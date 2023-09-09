import random

import pygame
pygame.init()

bg = pygame.image.load("../assets/old_assets/UPenn Cafe Pixel.jpg")
bg = pygame.transform.scale(bg, (800, 600))

waiter = pygame.image.load("../assets/old_assets/Waiter.jpg")
waiter = pygame.transform.scale(waiter, (50, 50))

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Restaurant Game")
pygame.display.set_icon(bg)

clock = pygame.time.Clock()

x_collide = False
y_collide = False

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

class RedKitchen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((WINDOW_WIDTH / 8, WINDOW_HEIGHT*3/4))
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(0, WINDOW_HEIGHT/8, WINDOW_WIDTH / 8, WINDOW_HEIGHT*3/4)
        self.image.fill((255, 0, 0))

        # self.rect1 = pygame.Rect(0, 0, WINDOW_WIDTH * 3 / 4, WINDOW_HEIGHT / 8)
        # self.rect2 = pygame.Rect(0, 0, WINDOW_WIDTH / 8, WINDOW_HEIGHT)
        # self.rect3 = pygame.Rect(0, WINDOW_HEIGHT * 7 / 8, WINDOW_WIDTH * 3 / 4, WINDOW_HEIGHT / 8)
        # self.rect4 = pygame.Rect(WINDOW_WIDTH * 2 / 8, WINDOW_HEIGHT * 5 / 16, WINDOW_WIDTH * 3 / 8, WINDOW_HEIGHT * 3 / 8)
        # self.rect5 = pygame.Rect(WINDOW_WIDTH * 13 / 16, WINDOW_HEIGHT * 5 / 16, WINDOW_WIDTH * 1 / 8, WINDOW_HEIGHT * 3 / 8)

    def update(self):
        pass
        # self.rect.topleft = [0, 0]

class GreenKitchen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((WINDOW_WIDTH * 3 / 4, WINDOW_HEIGHT / 8))
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(0, 0, WINDOW_WIDTH * 3 / 4, WINDOW_HEIGHT / 8)
        self.image.fill((0, 255, 0))

        # self.rect1 = pygame.Rect(0, 0, WINDOW_WIDTH * 3 / 4, WINDOW_HEIGHT / 8)
        # self.rect2 = pygame.Rect(0, 0, WINDOW_WIDTH / 8, WINDOW_HEIGHT)
        # self.rect3 = pygame.Rect(0, WINDOW_HEIGHT * 7 / 8, WINDOW_WIDTH * 3 / 4, WINDOW_HEIGHT / 8)
        # self.rect4 = pygame.Rect(WINDOW_WIDTH * 2 / 8, WINDOW_HEIGHT * 5 / 16, WINDOW_WIDTH * 3 / 8, WINDOW_HEIGHT * 3 / 8)
        # self.rect5 = pygame.Rect(WINDOW_WIDTH * 13 / 16, WINDOW_HEIGHT * 5 / 16, WINDOW_WIDTH * 1 / 8, WINDOW_HEIGHT * 3 / 8)

    def update(self):
        pass
        # self.rect.topleft = [0, 0]

class BlueKitchen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((WINDOW_WIDTH * 3 / 4, WINDOW_HEIGHT / 8))
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(0, WINDOW_HEIGHT * 7 / 8, WINDOW_WIDTH * 3 / 4, WINDOW_HEIGHT / 8)
        self.image.fill((0, 0, 255))

        # self.rect1 = pygame.Rect(0, 0, WINDOW_WIDTH * 3 / 4, WINDOW_HEIGHT / 8)
        # self.rect2 = pygame.Rect(0, 0, WINDOW_WIDTH / 8, WINDOW_HEIGHT)
        # self.rect3 = pygame.Rect(0, WINDOW_HEIGHT * 7 / 8, WINDOW_WIDTH * 3 / 4, WINDOW_HEIGHT / 8)
        # self.rect4 = pygame.Rect(WINDOW_WIDTH * 2 / 8, WINDOW_HEIGHT * 5 / 16, WINDOW_WIDTH * 3 / 8, WINDOW_HEIGHT * 3 / 8)
        # self.rect5 = pygame.Rect(WINDOW_WIDTH * 13 / 16, WINDOW_HEIGHT * 5 / 16, WINDOW_WIDTH * 1 / 8, WINDOW_HEIGHT * 3 / 8)

    def update(self):
        pass
        # self.rect.topleft = [0, 0]

class YellowKitchen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((WINDOW_WIDTH * 3 / 8, WINDOW_HEIGHT * 3 / 8))
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(WINDOW_WIDTH * 2 / 8, WINDOW_HEIGHT * 5 / 16, WINDOW_WIDTH * 3 / 8, WINDOW_HEIGHT * 3 / 8)
        self.image.fill((255, 255, 0))

        # self.rect1 = pygame.Rect(0, 0, WINDOW_WIDTH * 3 / 4, WINDOW_HEIGHT / 8)
        # self.rect2 = pygame.Rect(0, 0, WINDOW_WIDTH / 8, WINDOW_HEIGHT)
        # self.rect3 = pygame.Rect(0, WINDOW_HEIGHT * 7 / 8, WINDOW_WIDTH * 3 / 4, WINDOW_HEIGHT / 8)
        # self.rect4 = pygame.Rect(WINDOW_WIDTH * 2 / 8, WINDOW_HEIGHT * 5 / 16, WINDOW_WIDTH * 3 / 8, WINDOW_HEIGHT * 3 / 8)
        # self.rect5 = pygame.Rect(WINDOW_WIDTH * 13 / 16, WINDOW_HEIGHT * 5 / 16, WINDOW_WIDTH * 1 / 8, WINDOW_HEIGHT * 3 / 8)

    def update(self):
        pass
        # self.rect.topleft = [0, 0]

class PurpleKitchen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((WINDOW_WIDTH * 1 / 8, WINDOW_HEIGHT * 3 / 8))
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(WINDOW_WIDTH * 13 / 16, WINDOW_HEIGHT * 5 / 16, WINDOW_WIDTH * 1 / 8, WINDOW_HEIGHT * 3 / 8)
        self.image.fill((255, 0, 255))

        # self.rect1 = pygame.Rect(0, 0, WINDOW_WIDTH * 3 / 4, WINDOW_HEIGHT / 8)
        # self.rect2 = pygame.Rect(0, 0, WINDOW_WIDTH / 8, WINDOW_HEIGHT)
        # self.rect3 = pygame.Rect(0, WINDOW_HEIGHT * 7 / 8, WINDOW_WIDTH * 3 / 4, WINDOW_HEIGHT / 8)
        # self.rect4 = pygame.Rect(WINDOW_WIDTH * 2 / 8, WINDOW_HEIGHT * 5 / 16, WINDOW_WIDTH * 3 / 8, WINDOW_HEIGHT * 3 / 8)
        # self.rect5 = pygame.Rect(WINDOW_WIDTH * 13 / 16, WINDOW_HEIGHT * 5 / 16, WINDOW_WIDTH * 1 / 8, WINDOW_HEIGHT * 3 / 8)

    def update(self):
        pass
        # global y_collide
        # global x_collide
        #
        # if (player.rect.y + player.rect.height >= self.rect.y) or (player.rect.y <= self.rect.y + self.rect.height):
        #     y_collide = True
        # else:
        #     y_collide = False
        #
        # if (player.rect.x + player.rect.width >= self.rect.x) or (player.rect.x <= self.rect.x + self.rect.width):
        #     x_collide = True
        # else:
        #     x_collide = False

        # self.rect.topleft = [0, 0]

all_sprites = pygame.sprite.Group()
kitchens = pygame.sprite.Group()
player = Player(750, 500)

red_kitchen = RedKitchen()
green_kitchen = GreenKitchen()
blue_kitchen = BlueKitchen()
yellow_kitchen = YellowKitchen()
purple_kitchen = PurpleKitchen()

all_sprites.add(player)

kitchens.add(red_kitchen)
kitchens.add(green_kitchen)
kitchens.add(blue_kitchen)
kitchens.add(yellow_kitchen)
kitchens.add(purple_kitchen)





dt = 0
running = True

while running:

    screen.blit(bg, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.y -= 300 * dt
    if keys[pygame.K_a]:
        player.x -= 300 * dt
    if keys[pygame.K_s]:
        player.y += 300 * dt
    if keys[pygame.K_d]:
        player.x += 300 * dt

    for kitchen in kitchens:
        if (player.x + player.rect.width >= kitchen.rect.x) and \
            (player.y + player.rect.height >= kitchen.rect.y) and \
            (player.x <= kitchen.rect.x + kitchen.rect.width) and \
            (player.y <= kitchen.rect.y + kitchen.rect.height):

            # if (player.x + player.rect.width >= kitchen.rect.x):
            #     player.x = kitchen.rect.x + kitchen.rect.width
            # elif (player.y + player.rect.height >= kitchen.rect.y):
            #     player.y = kitchen.rect.y - player.rect.height
            # #
            # if (player.x + player.rect.width >= kitchen.rect.x) and (
            #         player.y + player.rect.height >= kitchen.rect.y):
            #
            #     # if y diff is less, player came from y, set their y to kitchen... vice versa

            top_y_diff = abs(kitchen.rect.y - (player.y + player.rect.height))
            bottom_y_diff = abs(player.y - (kitchen.rect.y + kitchen.rect.height))
            left_x_diff = abs(kitchen.rect.x - (player.rect.x + player.rect.width))
            right_x_diff = abs((kitchen.rect.x + kitchen.rect.width) - player.rect.x)

            diffs = [top_y_diff, bottom_y_diff, left_x_diff, right_x_diff]
            if min(diffs) == top_y_diff:
                print("top y")
                player.y = kitchen.rect.y - player.rect.height
            elif min(diffs) == bottom_y_diff:
                print("bottom y")
                player.y = kitchen.rect.y + kitchen.rect.height
            elif min(diffs) == left_x_diff:
                print("left x")
                player.x = kitchen.rect.x - player.rect.width
            elif min(diffs) == right_x_diff:
                print("right x")
                player.x = kitchen.rect.x + kitchen.rect.width


                # if abs(kitchen.rect.y - (player.y + player.rect.height)) < abs(
                #         kitchen.rect.x - (player.x + player.rect.width)):
                #     print("came from top y")
                # elif abs(player.y - kitchen.rect.y - kitchen.rect.height) < abs(
                #         player.x - kitchen.rect.x - kitchen.rect.width):
                #     print("came from bottom y")
                # # elif abs(kitchen.rect.x - (player.rect.x + player.rect.width))):
                # #     print('came from left x')
                # else:
                #     print('came from right x')
            #         # player_pos.y = kitchen.rect.y - self.rect.height
            #         player.x = kitchen.rect.x - player.rect.width
            #
            #     else:
            #         player.y = kitchen.rect.y - player.rect.height
            #
            # elif (player.x <= kitchen.rect.x + kitchen.rect.width) and (player.y <= kitchen.rect.y + kitchen.rect.height):
            # player.x = kitchen.rect.x - player.rect.width
            #     else:
            #         print('2')
            #         player.y = kitchen.rect.y + kitchen.rect.height
            #         # player.x = kitchen.rect.x + kitchen.rect.width
            #
            # else:
            #     if (player.y < kitchen.rect.y):
            #         print('3')
            #         player.y = kitchen.rect.y - player.rect.height
            #     else:
            #         print('4')
            #         # player.y = kitchen.rect.y + kitchen.rect.height
            #         player.x = kitchen.rect.x + kitchen.rect.width
            #
            # if (kitchen.rect.y + kitchen.rect.height - (player.y)) < (kitchen.rect.x + kitchen.rect.width - (player.x)):
            #     # player_pos.y = kitchen.rect.y - self.rect.height
            #     if (player.x > kitchen.rect.x):
            #         print('1')
            #         player.x = kitchen.rect.x - player.rect.width
            #     else:
            #         print('2')
            #         player.y = kitchen.rect.y + kitchen.rect.height
            #         # player.x = kitchen.rect.x + kitchen.rect.width
            #
            # else:
            #     if (player.y < kitchen.rect.y):
            #         print('3')
            #         player.y = kitchen.rect.y - player.rect.height
            #     else:
            #         print('4')
            #         # player.y = kitchen.rect.y + kitchen.rect.height
            #         player.x = kitchen.rect.x + kitchen.rect.width



    kitchens.update()
    kitchens.draw(screen)


    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.update()

    dt = clock.tick(60) / 1000