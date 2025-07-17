import pygame # type: ignore
from circleshape import CircleShape
from constants import *
import random
from explosion import Explosion


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)


    def update(self, dt):
        self.position += self.velocity * dt


    def split(self, shot):
        self.kill()
        shot.kill()

        # explosion effect for asteroids when shot
        for i in range(0, 20):
            explosion = Explosion(self.position.x, self.position.y)
            explosion.velocity = pygame.Vector2(0,1).rotate(i * 18) * EXPLOSION_SPEED
            explosion.timer = 0.3

        # split effect but only at a minimum size
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            vector1 = self.velocity.rotate(random_angle)
            vector2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = vector1 * 1.2
            asteroid2.velocity = vector2 * 1.2
