import pygame, thorpy as tp
import random
import pygame
import os

flag = True
difficulty = "EASY"

def first():
    pygame.init()
    W, H = 1200, 600
    screen = pygame.display.set_mode((W,H))
    tp.init(screen, tp.theme_human) #bind screen to gui elements and set theme

    bck = pygame.image.load("assets/welcome.png") #load some background pic for testing
    bck = pygame.transform.smoothscale(bck, (W,H))
    def before_gui(): #add here the things to do each frame before blitting gui elements
        screen.blit(bck, (0,0)) #blit background pic
    tp.call_before_gui(before_gui) #tells thorpy to call before_gui() before drawing gui.

    ddl1 = tp.DropDownListButton(("Easy / Untimed", "Hard / Timed"))
    ddl1_labelled = tp.Labelled("Choose Difficulty", ddl1)

    # ddl2 = tp.DropDownListButton(("One", "Two", "Three"), title="Two", choice_mode="h")

    choices = ("I want A!", "No, I want B.", "Actually, I do not know.")
    more_text = "Okay, tell me what you want."
    # alert = tp.AlertWithChoices("Some title", choices, more_text, choice_mode="h")
    alert = tp.Alert("Instructions and Controls", "Press e to pcik up food, Press g to give food to a customer", "Back")

    def my_func():
        alert.launch_alone() #see _example_launch for more options

    def get_difficulty():
        global difficulty
        print("User has chosen:", ddl1.get_value())
        if ddl1.get_value()[0] == 'E' or ddl1.get_value()[0] == 'N':
            difficulty = 'EASY'
        elif ddl1.get_value()[0] == 'H':
            difficulty = 'HARD'

        print(1 / 0)


    launcher = tp.Button("View Instructions and Controls")
    launcher.center_on(screen)
    launcher.at_unclick = my_func

    play_button = tp.Button("Play!")
    play_button.at_unclick = get_difficulty

    #all the arguments except the first one (the actual choices) are optional:
    ddl3 = tp.DropDownListButton(("Beginner", "Intermediate", "Expert", "Pro"),
                                    title=None, #by default, will take the first value
                                    choice_mode="v", #'v' for vertical or 'h' for horizontal
                                    align="left", #how to align choices in the list
                                    launch_nonblocking=False, #launch mode
                                    size_limit=("auto","auto"), #limit size of the list of options
                                    all_same_width=True, #all choices same width
                                    generate_shadow=(True, "auto"))#[0] : does generate shadow ? [1] : fast method or accurate method ? you can set [1] = "auto"

    ddl3_labelled = tp.Labelled("Third example", ddl3)

    group = tp.Box([ddl1_labelled, launcher, ddl3_labelled])
    group.center_on(screen)
    final_group = tp.Group([group, play_button])
    final_group.get_updater().launch()
    # launcher.get_updater().launch()
    pygame.quit()

while flag:
    try:
        first()
    except:
        break

print(difficulty)
pygame.init()

inventory = None

bg = pygame.image.load("assets/kitchen+counter_crop.png")
bg = pygame.transform.scale(bg, (1200, 600))

waiter = pygame.image.load("assets/people/Pizza_GuyMale.png")
waiter = pygame.transform.scale(waiter, (100, 100))

speech_bubble = pygame.image.load("assets/speech_bubble.png")
speech_bubble = pygame.transform.scale(speech_bubble, (100, 120))

customer_sprites = []
path = "assets/people"
dir_list = os.listdir(path)

for file in dir_list:
    img = pygame.image.load(path + "/" + file)
    img = pygame.transform.scale(img, (100, 100))
    customer_sprites.append(img)

breakfast_foods = []
path = "assets/breakfast"
dir_list = os.listdir(path)

for file in dir_list:
    img = pygame.image.load(path + "/" + file)
    img = pygame.transform.scale(img, (40, 40))
    breakfast_foods.append(img)

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Restaurant Game")
pygame.display.set_icon(bg)

clock = pygame.time.Clock()

class TimerBar(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, timer_width, time_limit):
        super().__init__()
        self.x = pos_x
        self.y = pos_y
        self.width = timer_width

        self.time_limit = time_limit
        self.time_left = time_limit

        self.time_up = False

        self.created = pygame.time.get_ticks()
        self.image = screen
        # self.image = pygame.Surface((self.width, 20))
        self.rect2 = pygame.draw.rect(self.image,
                                     "red",
                                     pygame.Rect(pos_x, pos_y, self.width, 20))
        self.rect = pygame.draw.rect(self.image,
                                     "green",
                                     pygame.Rect(pos_x, pos_y, self.width, 20))


    def update(self):
        self.rect2 = pygame.draw.rect(self.image,
                                     "red",
                                     pygame.Rect(self.x, self.y, self.width, 20))

        now = pygame.time.get_ticks()
        self.time_left = self.time_limit -(now - self.created)

        if (self.time_left <= 0):
            self.time_up = True
        else:
            self.rect = pygame.draw.rect(screen, "green",
                                         pygame.Rect(self.x, self.y, self.width * (self.time_left / self.time_limit),
                                                     20))

class BreakfastItem(pygame.sprite.Sprite):
    def __init__(self, x, y, index):
        super().__init__()

        self.x = x
        self.y = y
        self.image = breakfast_foods[index]
        self.food = "breakfast " + str(index)
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]

    def update(self):
        self.rect.topleft = [self.x, self.y]

class SpeechBubble(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y
        self.image = speech_bubble
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]

    def update(self):
        self.rect.topleft = [self.x, self.y]


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y
        self.image = waiter
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]

    def update(self):
        self.rect.topleft = [self.x, self.y]

        global inventory
        keys = pygame.key.get_pressed()

        # cookie = BreakfastItem(player.rect.x, player.rect.y - 20, 0)

        if inventory != None:
            if inventory == "breakfast 0":
                cookie_popup.x = player.x + 30
                cookie_popup.y = player.y - 30
                cookie_popup.update()
                inventory_sprites.add(cookie_popup)
            else:
                inventory_sprites.remove(cookie_popup)

            if inventory == "breakfast 1":
                egg_popup.x = player.x + 30
                egg_popup.y = player.y - 30
                egg_popup.update()
                inventory_sprites.add(egg_popup)
            else:
                inventory_sprites.remove(egg_popup)

            if inventory == "breakfast 2":
                muffin_popup.x = player.x + 30
                muffin_popup.y = player.y - 30
                muffin_popup.update()
                inventory_sprites.add(muffin_popup)
            else:
                inventory_sprites.remove(muffin_popup)

            if inventory == "breakfast 3":
                pancakes_popup.x = player.x + 30
                pancakes_popup.y = player.y - 30
                pancakes_popup.update()
                inventory_sprites.add(pancakes_popup)
            else:
                inventory_sprites.remove(pancakes_popup)

            if inventory == "breakfast 4":
                waffles_popup.x = player.x + 30
                waffles_popup.y = player.y - 30
                waffles_popup.update()
                inventory_sprites.add(waffles_popup)
            else:
                inventory_sprites.remove(waffles_popup)
        else:
            for sprite in inventory_sprites:
                sprite.kill()

        for station in all_stations:

            if (collide(player, station)):
                if fridges in station.groups():
                    # cookie.x = player.x
                    # cookie.y = player.y - 20
                    # if cookie not in all_sprites:
                    #     all_sprites.add(cookie)
                    # all_sprites.add(cookie)
                    # cookie.x = player.rect.x
                    # cookie.y = player.rect.y - 20

                    # if not (collide(player, fridge)):
                    if keys[pygame.K_e]:
                        inventory = "breakfast 0"
                        # inventory = breakfast_foods[0]

                if stoves in station.groups():
                    # if not (collide(player, stove)):
                    if keys[pygame.K_e]:
                        inventory = "breakfast 1"
                        # inventory = breakfast_foods[1]

                if sinks in station.groups():
                    # if not (collide(player, sink)):
                        if keys[pygame.K_e]:
                            inventory = "breakfast 2"
                            # inventory = breakfast_foods[4]

                if counters in station.groups():
                    # if not (collide(player, counter)):
                        if keys[pygame.K_e]:
                            inventory = "breakfast 3"
                            # inventory = breakfast_foods[3]

            # good
                if trays in station.groups():
                    # if not (collide(player, tray)):
                        if keys[pygame.K_e]:
                            inventory = "breakfast 4"
                            # inventory = breakfast_foods[2]

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, length, height):
        super().__init__()
        self.image = pygame.Surface((length, height))
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(x, y, length, height)

class Customer(pygame.sprite.Sprite):
    def __init__(self, ):
        super().__init__()
        self.x = 1300
        self.served = False
        self.order = None
        self.speech = None
        self.timer = None

        self.image = customer_sprites[random.randint(0, len(customer_sprites)-1)]
        self.right = self.image
        self.left = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()

        self.y = random.randint(front.rect.y, front.rect.y + front.rect.height - self.rect.height)

        self.rect.topleft = [self.x, self.y]
    def update(self):

        if self.timer is not None and self.timer.time_up:
            self.timer.kill()
            self.served = True
        if self.served:
            if self.timer is not None:
                self.timer.kill()
                self.timer = None
            if self.order is not None:
                self.order.kill()
                # self.order = None
            if self.speech is not None:
                self.speech.kill()
                self.speech = None

            self.image = self.right
            if self.rect.x + self.rect.width > 1200:
                self.kill()

            self.x += 5
            self.rect.topleft = [self.x, self.y]
        # if not self.served:
        else:
            self.image = self.left
            if (self.rect.x <= front.rect.x + front.rect.width + 4):
                self.rect.topleft = [self.x, self.y]
                if self.order is None:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_g]:
                        speech_bubble = SpeechBubble(customer.rect.x + 20, customer.rect.y - 100)
                        speech_bubbles.add(speech_bubble)
                        breakfast_item = BreakfastItem(customer.rect.x + 50, customer.rect.y - 65, random.randint(0, len(breakfast_foods)-1))
                        breakfasts.add(breakfast_item)

                        if difficulty == "HARD":
                            self.timer = TimerBar(self.x, self.y - 20, 100, 5000)
                            timers.add(self.timer)

                        self.order = breakfast_item
                        self.speech = speech_bubble

            elif not (self.served):
                self.x -= 5
                self.rect.topleft = [self.x, self.y]




all_sprites = pygame.sprite.Group()
kitchens = pygame.sprite.Group()
player = Player(600, 300)

all_sprites.add(player)

cookie_popup = BreakfastItem(player.rect.x, player.rect.y - 20, 0)
egg_popup = BreakfastItem(player.rect.x, player.rect.y - 20, 1)
muffin_popup = BreakfastItem(player.rect.x, player.rect.y - 20, 2)
pancakes_popup = BreakfastItem(player.rect.x, player.rect.y - 20, 3)
waffles_popup = BreakfastItem(player.rect.x, player.rect.y - 20, 4)


walls = pygame.sprite.Group()
wall1 = Wall(41, 44, 10, 515)
wall2 = Wall(41, 44, 907, 10)
wall3 = Wall(41, 545, 907, 14)
wall4 = Wall(938, 44, 10, 165)
wall5 = Wall(938, 345, 10, 200)
wall6 = Wall(441, 370, 15, 180)
wall7 = Wall(942, 130, 68, 10)
wall8 = Wall(942, 440, 68, 10)


walls.add(wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8)

fridges = pygame.sprite.Group()
fridge1 = Wall(51, 54, 80, 80)
fridge2 = Wall(51, 134, 120, 190)

fridges.add(fridge1, fridge2)

stove = Wall(51, 425, 377, 120)
stoves = pygame.sprite.Group()
stoves.add(stove)

tray = Wall(324, 54, 99, 190)
trays = pygame.sprite.Group()
trays.add(tray)

counter1 = Wall(423, 54, 425, 86)
counter2 = Wall(848, 54, 90, 155)
counters = pygame.sprite.Group()
counters.add(counter1, counter2)

sink = Wall(468, 459, 470, 86)
sinks = pygame.sprite.Group()
sinks.add(sink)

front = Wall(1010, 130, 68, 320)
fronts = pygame.sprite.Group()
fronts.add(front)

all_stations = pygame.sprite.Group()
for station in fridges:
    all_stations.add(station)
for station in stoves:
    all_stations.add(station)
for station in counters:
    all_stations.add(station)
for station in sinks:
    all_stations.add(station)
for station in trays:
    all_stations.add(station)

customers = pygame.sprite.Group()
speech_bubbles = pygame.sprite.Group()
breakfasts = pygame.sprite.Group()
timers = pygame.sprite.Group()
inventory_sprites = pygame.sprite.Group()

kitchen_item_1 = BreakfastItem(87, 190, 0)
kitchen_item_12 = BreakfastItem(87, 210, 0)
kitchen_item_13 = BreakfastItem(87, 230, 0)
kitchen_item_2 = BreakfastItem(320, 470, 1)
kitchen_item_21 = BreakfastItem(150, 450, 1)
kitchen_item_22 = BreakfastItem(200, 485, 1)
kitchen_item_3 = BreakfastItem(705, 480, 2)
kitchen_item_31 = BreakfastItem(768, 480, 2)
kitchen_item_4 = BreakfastItem(500, 80, 3)
kitchen_item_41 = BreakfastItem(600, 60, 3)
kitchen_item_42 = BreakfastItem(650, 90, 3)
kitchen_item_43 = BreakfastItem(720, 90, 3)
kitchen_item_5 = BreakfastItem(355, 90, 4)
kitchen_item_51 = BreakfastItem(355, 140, 4)


all_sprites.add(kitchen_item_1,
                kitchen_item_12,
                kitchen_item_13,
                kitchen_item_2,
                kitchen_item_21,
                kitchen_item_22,
                kitchen_item_3,
                kitchen_item_31,
                kitchen_item_4,
                kitchen_item_41,
                kitchen_item_42,
                kitchen_item_43,
                kitchen_item_5,
                kitchen_item_51)


dt = 0
running = True

NEW_CUSTOMER = pygame.USEREVENT + 1

pygame.time.set_timer(NEW_CUSTOMER, 5000)


def collide(rect1, rect2):
    if (rect1.x + rect1.rect.width >= rect2.rect.x) and \
            (rect1.y + rect1.rect.height >= rect2.rect.y) and \
            (rect1.x <= rect2.rect.x + rect2.rect.width) and \
            (rect1.y <= rect2.rect.y + rect2.rect.height):

        top_y_diff = abs(rect2.rect.y - (rect1.y + rect1.rect.height))
        bottom_y_diff = abs(rect1.y - (rect2.rect.y + rect2.rect.height))
        left_x_diff = abs(rect2.rect.x - (rect1.rect.x + rect1.rect.width))
        right_x_diff = abs((rect2.rect.x + rect2.rect.width) - rect1.rect.x)

        diffs = [top_y_diff, bottom_y_diff, left_x_diff, right_x_diff]
        if min(diffs) == top_y_diff:
            # print("top y")
            rect1.y = rect2.rect.y - rect1.rect.height
        elif min(diffs) == bottom_y_diff:
            # print("bottom y")
            rect1.y = rect2.rect.y + rect2.rect.height
        elif min(diffs) == left_x_diff:
            # print("left x")
            rect1.x = rect2.rect.x - rect1.rect.width
        elif min(diffs) == right_x_diff:
            # print("right x")
            rect1.x = rect2.rect.x + rect2.rect.width
        else:
            return False

        return True

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

dialogue_box_width = 1200
dialogue_box_height = 150
dialogue_box_x = (1200 - dialogue_box_width) // 2
dialogue_box_y = (600 - dialogue_box_height)

display_dialogue = 0

while running:

    screen.blit(bg, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == NEW_CUSTOMER:
            if difficulty == "EASY":
                if(len(customers.sprites())) > 0:
                    pass
                else:
                    customer = Customer()
                    customers.add(customer)


            if difficulty == "HARD":
                customer = Customer()
                customers.add(customer)

        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_g]:
                print(display_dialogue)
                display_dialogue += 1



    all_sprites.update()
    all_sprites.draw(screen)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.y -= 1000 * dt
    if keys[pygame.K_a]:
        player.image = pygame.transform.flip(waiter, True, False)
        player.x -= 1000 * dt
    if keys[pygame.K_s]:
        player.y += 1000 * dt
    if keys[pygame.K_d]:
        player.image = pygame.transform.flip(waiter, False, False)
        player.x += 1000 * dt
    if keys[pygame.K_g]:
        if player.rect.x + player.rect.width == front.rect.x:
            if len(customers.sprites()) > 0:
                first_customer = customers.sprites()[0]
                try:
                    if inventory == first_customer.order.food:
                        first_customer.served = True
                        display_dialogue = 1
                        customers.update()
                        inventory = None
                except AttributeError:
                    pass
                    # customer hasnt reached table yet

    for wall in walls:
        collide(player, wall)

    for fridge in fridges:
        collide(player, fridge)

    for stove in stoves:
        collide(player, stove)

    for tray in trays:
        collide(player, tray)

    for counter in counters:
        collide(player, counter)

    for sink in sinks:
        collide(player, sink)

    for front in fronts:
        if(collide(player, front)):
            if display_dialogue % 2 == 0:
                if len(customers.sprites()) > 0:
                    font = pygame.font.Font(
                        "assets/victor-pixel.ttf", 24)
                    text_color = "BLACK"
                    pygame.draw.rect(screen, GRAY, (dialogue_box_x,
                                                    dialogue_box_y,
                                                    dialogue_box_width,
                                                    dialogue_box_height))

                    # Add text to the dialog box
                    text = "Please, I want one hamburger."
                    rendered_text = font.render(text, True, text_color)
                    text_rect = rendered_text.get_rect(center=(dialogue_box_x + dialogue_box_width // 2,
                                                               dialogue_box_y + dialogue_box_height // 2))
                    screen.blit(rendered_text, text_rect)
        else:
            display_dialogue = 1

    # customers.update()
    for i in range(len(customers.sprites())):

        index = len(customers.sprites()) - 1 - i
        customer = customers.sprites()[index]
        customer.update()
        screen.blit(customer.image, (customer.rect.x, customer.rect.y))
    # customers.draw(screen)

    for i in range(len(timers.sprites())):
        index = len(timers.sprites()) - 1 - i
        timers.sprites()[index].update()
    # timers.draw(screen)

    if len(breakfasts.sprites()) > 0:
        # for i in range(len(speech_bubbles.sprites())):
        for j in range(len(speech_bubbles.sprites())):
            i = len(speech_bubbles.sprites()) - 1 - j
            current_speech_bubble = speech_bubbles.sprites()[i]
            current_speech_bubble.update()
            screen.blit(current_speech_bubble.image, (current_speech_bubble.rect.x, current_speech_bubble.rect.y))

        # for j in range(len(breakfasts.sprites())):
        #     i = len(breakfasts.sprites()) - 1 - j
            current_breakfast_item = breakfasts.sprites()[i]
            current_breakfast_item.update()
            screen.blit(current_breakfast_item.image, (current_breakfast_item.rect.x, current_breakfast_item.rect.y))

    pygame.draw.rect(screen, "black", pygame.Rect(942, 130, 68, 10))
    pygame.draw.rect(screen, "black", pygame.Rect(942, 440, 68, 10))

    inventory_sprites.update()
    inventory_sprites.draw(screen)

    # all_sprites.update()
    # all_sprites.draw(screen)

    pygame.display.update()

    dt = clock.tick(60) / 1000