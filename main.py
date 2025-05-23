import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    FPS = pygame.time.Clock()
    dt = 0

    # Set up the containers for the player
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    # Set up the containers for the asteroids
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    # Set up the containers for the asteroid field
    AsteroidField.containers = updatable

    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((0, 0, 0))
        updatable.update(dt)
        for drawable_object in drawable:
            drawable_object.draw(screen)
        pygame.display.flip()
        dt = FPS.tick(60) / 1000  # Convert milliseconds to seconds


if __name__ == "__main__":
    main()
