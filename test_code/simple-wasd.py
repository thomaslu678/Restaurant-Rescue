# Example file showing a circle moving on screen
import time

import pygame
import random
import threading

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 533))
customers = pygame.surface.Surface((100, 100))
clock = pygame.time.Clock()


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

def print_a(wait):
    while True:
        time.sleep(wait)

        customer = pygame.image.load("../assets/old_assets/Customer Pixel.jpg")

        pygame.draw.circle(customers, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                           , player_pos, 40)

        customers.blit(customer, (100, 200))

        print("looped")


def run_character():
    dt = 0
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        bg = pygame.image.load("../assets/old_assets/UPenn Cafe Pixel.jpg")

        # fill the screen with a color to wipe away anything from last frame
        screen.blit(bg, (0,0))
        screen.blit(customers, (50, 50))

        pygame.draw.circle(screen, "red", player_pos, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

t1 = threading.Thread(target=print_a, args=(3,))

t1.start()

run_character()







pygame.quit()