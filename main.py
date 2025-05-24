import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Shot


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

    # Set up the containers for the bullets
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    # Load font for score display
    score_font = pygame.font.Font(None, 36)
    score = 0

    # Add lives counter
    lives_font = pygame.font.Font(None, 36)
    lives = 3

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((0, 0, 0))
        updatable.update(dt)
        for asteroid in asteroids:
            # Check for collisions with the player
            if asteroid.check_collision(player):
                lives -= 1
                player.kill()  # Remove player from the game
                if lives > 0:
                    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                else:
                    print("Game over!")
                    pygame.quit()
                    return
            # Check for collisions with shots
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()
                    score += 1
                    break

        for drawable_object in drawable:
            drawable_object.draw(screen)
        # Draw the score and lives
        score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
        lives_text = lives_font.render(f"Lives: {lives}", True, (255, 255, 255))
        screen.blit(lives_text, (10, 40))
        screen.blit(score_text, (10, 10))
        pygame.display.flip()
        dt = FPS.tick(60) / 1000  # Convert milliseconds to seconds


if __name__ == "__main__":
    main()
