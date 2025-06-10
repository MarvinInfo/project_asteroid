# shot.py

import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape, pygame.sprite.Sprite):
    containers = ()  # Will be set externally in main.py

    def __init__(self, x, y, direction_vector):
        super().__init__(x, y, SHOT_RADIUS)
        pygame.sprite.Sprite.__init__(self, self.containers)

        # Scale direction vector to shooting speed
        self.velocity = direction_vector.normalize() * 500  # or use PLAYER_SHOOT_SPEED if imported
       
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0, 0), (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
