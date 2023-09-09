import pygame, sys
import os
import random

img = pygame.image.load("../assets/old_assets/Customer Pixel.jpg")
img = pygame.transform.scale(img, (100, 100))

table = pygame.image.load("../assets/old_assets/Table.jpg")
table = pygame.transform.scale(table, (100, 100))

bg = pygame.image.load("../assets/old_assets/UPenn Cafe Pixel.jpg")

path = "../assets/foods"
dir_list = os.listdir(path)

food_images = []

for file in dir_list:
    img = pygame.image.load(path + "/" + file)
    img = pygame.transform.scale(img, (20, 20))
    food_images.append(img)

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


class TimerBar(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, timer_width, time_limit):
        super().__init__()
        self.x = pos_x
        self.y = pos_y
        self.width = timer_width

        self.time_limit = time_limit
        self.time_left = time_limit

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
            timers.remove(self)
            # send mf home
        else:
            self.rect = pygame.draw.rect(screen, "green",
                                         pygame.Rect(self.x, self.y, self.width * (self.time_left / self.time_limit),
                                                     20))


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.x = pos_x
        self.y = pos_y

        self.created = pygame.time.get_ticks()
        self.wait_time = 5000

        # self.image = pygame.Surface([20, 20])
        # self.image.fill((255, 0, 0))
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]

    def update(self):
        self.x += 1
        self.rect.topleft = [self.x, self.y]

        # print("created", self.created)
        now = pygame.time.get_ticks()
        # print(now)
        if now - self.created >= self.wait_time:
            self.created = now
            print("if")

    def check_collision(self, other_rect):
        if self.rect.colliderect(other_rect):
            other_rect.image = table

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()

player = Player(100, 100)
moving_sprites.add(player)

obstacle = Player(300, 100)
moving_sprites.add(obstacle)

menu = Menu(100, 100)
menus = pygame.sprite.Group()
menus.add(menu)

timer = TimerBar(50, 50, 100, 5000)
timers = pygame.sprite.Group()
timers.add(timer)

while True:

    screen.blit(bg, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                menu.current_image -= 1
            if event.key == pygame.K_DOWN:
                menu.current_image += 1

    player.update()
    player.check_collision(obstacle)

    timers.update()
    # timers.draw(screen)



    menus.update()
    menus.draw(screen)

    # Drawing
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
