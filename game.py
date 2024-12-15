import pygame
import random
import sys
import time

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('First Game')

def main():
    clock = pygame.time.Clock()

    GAMELOOP = False
    FPS = 60
    RED = 255
    GREEN = 200
    BLUE = 100
    X = 100
    velocity = 5

    while not GAMELOOP:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAMELOOP = True

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            X -= velocity

        if keys[pygame.K_RIGHT]:
            X += velocity

        if X < 0:
            GAMELOOP = True

        screen.fill((10, 100, 200))

        pygame.draw.rect(screen, (RED, GREEN, BLUE), (X, 540, 50, 50))

        pygame.display.flip()

        clock.tick(FPS)

if __name__ == '__main__':
    main()