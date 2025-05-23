import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    FPS = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((0, 0, 0))
        player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        player.draw(screen)
        pygame.display.flip()
        dt = FPS.tick(60) / 1000  # Convert milliseconds to seconds


if __name__ == "__main__":
    main()
