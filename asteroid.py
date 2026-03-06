import pygame

import random

from circleshape import CircleShape

from constants import SCREEN_HEIGHT, SCREEN_WIDTH, LINE_WIDTH, ASTEROID_MIN_RADIUS

from logger import log_event

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            ran_angle = random.uniform(20, 50)
            self.new_velocity1 = pygame.math.Vector2.rotate(self.velocity, ran_angle)
            self.new_velocity2 = pygame.math.Vector2.rotate(self.velocity, -ran_angle)
            self.new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, self.new_radius)
            new_asteroid1.velocity = self.new_velocity1 * 1.2
            new_asteroid2 = Asteroid(self.position.x, self.position.y, self.new_radius)
            new_asteroid2.velocity = self.new_velocity2 * 1.2

