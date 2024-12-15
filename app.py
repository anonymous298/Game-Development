from turtle import Screen, screensize
import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()

    def start_game_loop(self):
        screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption('My first Pygame window')

        clock = pygame.time.Clock()

        X, Y = 100, 100
        velocity = 5

        FPS = 120
        RED = 0
        GREEN = 128
        BLUE = 255

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        print('Up Key pressed')

                    elif event.key == pygame.K_DOWN:
                        print('Down Key pressed')

                    elif event.key == pygame.K_LEFT:
                        print('Left Key Pressed')

                    elif event.key == pygame.K_RIGHT:
                        print('Right Key Pressed')

                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(f'Mouse Button Cliced at <{event.pos}>')

            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                Y -= velocity

            if keys[pygame.K_DOWN]:
                Y += velocity

            if keys[pygame.K_LEFT]:
                X -= velocity

            if keys[pygame.K_RIGHT]:
                X += velocity

            screen.fill((RED, GREEN, BLUE))
            pygame.draw.rect(screen, (255, 0, 0), (X, Y, 50, 50))

            pygame.display.flip()

            clock.tick(FPS)


game = Game()
game.start_game_loop()