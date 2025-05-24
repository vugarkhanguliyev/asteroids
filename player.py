from circleshape import CircleShape
from constants import *
import pygame
from bullet import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, radius=PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0.0
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = 300
        self.friction = 0.98

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # Rotate left
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # Rotate right
            self.rotate(dt)
        if keys[pygame.K_w]:
            # Move forward
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.velocity += forward * self.acceleration * dt
        if keys[pygame.K_s]:
            # Move backward
            backward = pygame.Vector2(0, 1).rotate(self.rotation + 180)
            self.velocity += backward * self.acceleration * dt
        if keys[pygame.K_SPACE]:
            # Shoot
            if self.timer <= 0:
                self.timer = PLAYER_SHOOT_COOLDOWN
                return self.shoot()
            else:
                self.timer -= dt
        else:
            if self.timer > 0:
                self.timer -= dt

        # Apply friction
        self.velocity *= self.friction
        # Update position
        self.position += self.velocity * dt

    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot = Shot(
            self.position.x + forward.x * self.radius,
            self.position.y + forward.y * self.radius,
        )
        shot.velocity += forward * PLAYER_SHOOT_SPEED
        return shot
