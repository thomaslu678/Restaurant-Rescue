"""

Controls

wasd to move

customers are seated at random with a random order

when you collide with the kitchen, a menu will appear
you can change the food to be prepared using up/down arrow keys
hit the zero key to start preparing the order

once the food is ready (kitchen bar is gone), hit he m key to pick up the food

now you can feed it to a customer with that order using the g key

the bar above each customer shows its patience level; when it reaches zero, they leave

"""


import random
import os


import pygame
pygame.init()

bg = pygame.image.load("assets/old_assets/UPenn Cafe Pixel.jpg")

customer_image = pygame.image.load("assets/old_assets/Customer Pixel.jpg")
customer_image = pygame.transform.scale(customer_image, (100, 100))

empty_table = pygame.image.load("assets/old_assets/Table.jpg")
empty_table = pygame.transform.scale(empty_table, (100, 100))

occupied_table = pygame.image.load("assets/old_assets/Occupied Table.jpg")
occupied_table = pygame.transform.scale(occupied_table, (100, 100))

kitchen_image = pygame.image.load("assets/old_assets/Kitchen.jpg")
kitchen_image = pygame.transform.scale(kitchen_image, (400, 150))

waiter = pygame.image.load("assets/old_assets/Waiter.jpg")
waiter = pygame.transform.scale(waiter, (50, 50))

path = "assets/foods"
dir_list = os.listdir(path)

food_images = []

for file in dir_list:
    img = pygame.image.load(path + "/" + file)
    img = pygame.transform.scale(img, (20, 20))
    food_images.append(img)

WINDOW_LENGTH = 800
WINDOW_WIDTH = 533

screen = pygame.display.set_mode((WINDOW_LENGTH, WINDOW_WIDTH))
pygame.display.set_caption("Restaurant Game")
pygame.display.set_icon(bg)

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
clock = pygame.time.Clock()

now = pygame.time.get_ticks()

def get_now():
    now = pygame.time.get_ticks()
    return now

class Menu(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.x = pos_x
        self.y = pos_y

        self.images = food_images
        self.current_image = 1

        self.image = food_images[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]

    def update(self):

        if self.current_image == -1:
            self.current_image = 2
        if self.current_image == 3:
            self.current_image = 0

        self.image = food_images[self.current_image]

class Order(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.x = pos_x
        self.y = pos_y

        # self.image = pygame.Surface([20, 20])
        # self.image.fill((255, 0, 0))
        self.image = food_images[random.randint(0, len(food_images)-1)]
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]

    def update(self):
        self.rect.topleft = [self.x, self.y]

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


inventory = None

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # self.image = pygame.Surface([20, 20])
        # self.image.fill((255, 0, 0))
        self.image = waiter
        self.rect = self.image.get_rect()
        self.rect.topleft = [player_pos.x, player_pos.y]

    def update(self):
        self.rect.topleft = [player_pos.x, player_pos.y]
        global inventory


        # if self.rect.colliderect(kitchen.rect):
        if (player_pos.x + self.rect.width >= kitchen.rect.x) and (player_pos.y + self.rect.height >= kitchen.rect.y):

            # if y diff is less, player came from y, set their y to kitchen... vice versa
            if (kitchen.rect.y - (player_pos.y + self.rect.height)) < (kitchen.rect.x - (player_pos.x + self.rect.width)):
                # player_pos.y = kitchen.rect.y - self.rect.height
                player_pos.x = kitchen.rect.x - self.rect.width

            else:
                player_pos.y = kitchen.rect.y - self.rect.height
                # player_pos.x = kitchen.rect.x - self.rect.width

            menus.add(menu)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_0]:
                kitchen.order = menu.image
                # kitchen.order = food_images[0]
                kitchen.update()
            if keys[pygame.K_x]:
                kitchen.order = None
                timers.remove(kitchen.timer)
                kitchen.timer = None
        else:
            menus.remove(menu)

        for i in range(len(taken_seats)):
            seat = taken_seats[i]
            if self.rect.colliderect(seat.rect):

                keys = pygame.key.get_pressed()
                if keys[pygame.K_g]:
                    try:
                        if (inventory == seat.order.image):
                            seat.taken = False
                            orders.remove(seat.order)
                            inventory = None
                            seat.served = True
                            seats.update()
                            customers.update()

                            print('happy customer')

                            # need to send the customer home, then remove
                    except AttributeError:
                        pass

                    """
                                        except AttributeError:

                        # customer hasn't reached seat yet
                        # user should not be able to give food yet
                        pass
                    """

                # if keys[pygame.K_0]:
                #     inventory = food_images[0]
                # if keys[pygame.K_1]:
                #     inventory = food_images[1]
                # if keys[pygame.K_2]:
                #     inventory = food_images[2]


# Object class
class Customer(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, seat):
        super().__init__()
        self.seat = seat
        if (empty_seats[self.seat].served == True):
            self.x = empty_seats[self.seat].rect.x
            self.y = empty_seats[self.seat].rect.y
        else:
            self.x = pos_x
            self.y = pos_y

        # self.image = pygame.Surface([20, 20])
        # self.image.fill((255, 0, 0))
        self.image = customer_image
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]

    def update(self):
        # target_seat = seats.sprites()[seat_number]
        # target_seat = seats.sprites()[self.seat]

        target_seat = empty_seats[self.seat]


        # Ensure the input seat_number is not taken (logic before

        # if self.x < seats.sprites()[seat_number].rect.x:
        if (target_seat.served): # or time expires out
            #self.x = target_seat.rect.x
            #self.y = target_seat.rect.y
            self.send_home(target_seat)
        else:
            if not (self.rect.colliderect(target_seat.rect)):
                self.x += 20
            else:
                target_seat.taken = True
                target_seat.update()
                customers.remove(self)
        self.rect.topleft = [self.x, self.y]

        # if not (self.rect.colliderect(seats.sprites()[seat_number].rect)):
            # print("collided!")

    def send_home(self, target_seat):
        customers.add(self)
        self.x -= 20
        if (self.x <= 0):
            customers.remove(self)
            target_seat.served = False


class Seat(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.taken = False
        self.x = pos_x
        self.y = pos_y
        self.order = None
        self.timer = None
        self.served = False

        self.time_seated = pygame.time.get_ticks()
        self.wait_time = 20000

        # self.image = pygame.Surface([50, 50])
        # self.image.fill((0, 255, 0))
        self.image = empty_table

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]

    def update(self):

        if self.taken:
            self.image = occupied_table
            if self.order is None:
                self.order = Order(self.x+20, self.y-20)
                orders.add(self.order)

                self.timer = TimerBar(self.x+20, self.y+10, 100, self.wait_time)
                timers.add(self.timer)

                self.time_seated = pygame.time.get_ticks()
            self.check_wait_time()

        else:
            self.image = empty_table
            self.order = None
            orders.remove(self.order)
            timers.remove(self.timer)

        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]

    def check_wait_time(self):
        if get_now() - self.time_seated >= self.wait_time:
            self.time_seated = get_now()
            # print(self.x, "go home")

            self.taken = False
            orders.remove(self.order)
            # timers.remove(self.timer)
            self.served = True

            # customers.update()


class Kitchen(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.taken = False
        self.x = pos_x
        self.y = pos_y
        self.order = None
        self.timer = None
        self.ready_food = None

        self.image = kitchen_image
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]

    def update(self):

        if (self.order is not None):
            if (self.timer is None):
                self.timer = TimerBar(self.x, self.y - 20, 100, 5000)
                timers.add(self.timer)

            if self.timer.time_up == True:
                self.ready_food = self.order

                self.order = None
                timers.remove(self.timer)
                self.timer = None
        if self.ready_food is not None:
            if (player_pos.x + player.rect.width >= self.rect.x) and (player_pos.y + player.rect.height >= self.rect.y):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_m]:
                    global inventory
                    inventory = self.ready_food
                    self.ready_food = None



# GLOBAL VARIABLES
COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
WIDTH = 500
HEIGHT = 500

customers = pygame.sprite.Group()
seats = pygame.sprite.Group()
for i in range(4):
    seat = Seat(100 + i * 150, 20)
    seats.add(seat)

player_group = pygame.sprite.Group()
orders = pygame.sprite.Group()
timers = pygame.sprite.Group()
kitchens = pygame.sprite.Group()
menus = pygame.sprite.Group()



# Object class

NEW_CUSTOMER = pygame.USEREVENT + 1

pygame.time.set_timer(NEW_CUSTOMER, 1500)

empty_seats = []
for i in range(len(seats.sprites())):
    seat = seats.sprites()[i]
    if not seat.taken:
        empty_seats.append(seat)

kitchen = Kitchen(400, 383)
kitchens.add(kitchen)

menu = Menu(kitchen.rect.x, kitchen.rect.y + 20)

taken_seats = []

player = Player()
player_group.add(player)


dt = 0
running = True



while running:

    screen.blit(bg, (0, 0))

    for event in pygame.event.get():

        if event.type == NEW_CUSTOMER:

            empty_seats = []

            for i in range(len(seats.sprites())):
                seat = seats.sprites()[i]
                if not seat.taken:
                    empty_seats.append(seat)

            if len(empty_seats) > 0:

                index = 0

                if len(empty_seats) >= 1:
                    index = random.randint(0, len(empty_seats) - 1)
                # print(index)

                rand_x = random.randint(0, 800)
                rand_y = random.randint(0, 533)
                taken_seats.append(empty_seats[index])

                customer = Customer(20, 20, index)
                # print(len(taken_seats))

                customers.add(customer)

                customer.rect.x = rand_x
                customer.rect.y = rand_y
            else:
                print("no more seats")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                menu.current_image -= 1
            if event.key == pygame.K_DOWN:
                menu.current_image += 1

        if event.type == pygame.QUIT:
            running = False



    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if player_pos.y >= 0:
            player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        if player_pos.y + player.rect.height <= WINDOW_WIDTH:
            player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        if player_pos.x + player.rect.width <= WINDOW_LENGTH:
            player_pos.x += 300 * dt



    # flip() the display to put your work on screen
    # pygame.display.flip()



    player_group.update()
    player_group.draw(screen)

    seats.update()
    seats.draw(screen)

    orders.update()
    orders.draw(screen)

    kitchens.update()
    kitchens.draw(screen)

    menus.update()
    menus.draw(screen)

    timers.update()

    customers.update()
    customers.draw(screen)

    pygame.display.flip()
    pygame.display.update()

    dt = clock.tick(60) / 1000
