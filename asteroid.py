from circleshape import *
from typing import ClassVar,Tuple
from pygame import*
from constants import *
import random,math

class Asteroid(CircleShape):

    containers: ClassVar[Tuple[pygame.sprite.Group, ...]] = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.radius = radius


    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # Always remove this asteroid
        self.kill()

        # If it's already small, stop here
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Create two smaller asteroids
        angle = random.uniform(20, 50)  # degrees
        velocity1 = self.velocity.rotate(angle) * 1.2
        velocity2 = self.velocity.rotate(-angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Spawn two new asteroids at the same position
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = velocity1

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = velocity2