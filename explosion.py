import pygame # type: ignore
from circleshape import CircleShape
from constants import *
import random


class Explosion(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, EXPLOSION_RADIUS)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, EXPLOSION_RADIUS, 2)

    
    def update(self, dt):
        self.position += self.velocity * dt
        self.timer -= dt
        if self.timer <= 0:
            self.kill()