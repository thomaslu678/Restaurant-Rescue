import random

import pygame
pygame.init()

bg = pygame.image.load("../assets/old_assets/UPenn Cafe Pixel.jpg")

waiter = pygame.image.load("../assets/old_assets/Waiter.jpg")
waiter = pygame.transform.scale(waiter, (50, 50))

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 533

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Restaurant Game")
pygame.display.set_icon(bg)

clock = pygame.time.Clock()

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

all_sprites = pygame.sprite.Group()
player = Player(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
all_sprites.add(player)


dt = 0
running = True

while running:

    image = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    if player.x <= 0:
        player.x = 0
    if player.y <= 0:
        player.y = 0
    if player.x + player.rect.width >= bg.get_width():
        player.x = bg.get_width() - player.rect.width
    if player.y + player.rect.height >= bg.get_height():
        player.y = bg.get_height() - player.rect.height

    # if player.x = 680

    if player.x <= 300:
        image.blit(bg, (0, 0))
    elif player.x > 300 and player.x < (WINDOW_WIDTH-300):
        image.blit(bg, (300 - player.x, 0))

    screen.blit(image, (0, 0))

    # if player.x + player.rect.width + 100 >= WINDOW_WIDTH:
    #     print(player.x + player.rect.width + 100 - WINDOW_WIDTH)
    #     image.blit(bg, (-((player.x + player.rect.width + 100 - WINDOW_WIDTH)), 0))
    # # # if player.y >= WINDOW_HEIGHT:
    # #     image.blit(bg, (0, WINDOW_HEIGHT - player.y))
    # else:
    #     image.blit(bg, (0, 0))
    #
    # screen.blit(image, (0, 0))

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

    pygame.draw.rect(screen, (0, 0, 0), (player.x - 300, 0, 600, 533), 3)  # width = 3

    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.update()

    dt = clock.tick(60) / 1000
