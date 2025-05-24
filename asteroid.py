from circleshape import CircleShape
import pygame
import random
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(self.position.x), int(self.position.y)),
            self.radius,
            2,
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        """Split the asteroid into two smaller ones."""
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            # Create two new asteroids with half the radius
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            random_angle = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(random_angle)
            velocity2 = self.velocity.rotate(-random_angle)
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = (
                velocity1 * 1.2
            )  # Slightly increase speed of new asteroids
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = (
                velocity2 * 1.2
            )  # Slightly increase speed of new asteroids
            # Return the two new asteroids
            return [asteroid1, asteroid2]
        else:
            return []
