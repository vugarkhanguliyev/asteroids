from circleshape import CircleShape
import pygame
from constants import *


class Shot(CircleShape):
    def __init__(self, x, y, radius=SHOT_RADIUS):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 0),
            (int(self.position.x), int(self.position.y)),
            self.radius,
            0,
        )

    def update(self, dt):
        self.position += self.velocity * dt
