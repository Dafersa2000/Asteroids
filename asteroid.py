import pygame
import circleshape
from constants import COLOR, LINE_WIDTH, ASTEROID_SPEED_INCREASE, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
import random
import logger

class Asteroid(circleshape.CircleShape):
    def __init__(self, x:float, y:float, radius:float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, COLOR, self.position, self.radius,LINE_WIDTH)

    def update(self, dt):
         self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            pass
        elif self.radius > ASTEROID_MIN_RADIUS:
            logger.log_event("asteroid_split")
            angle = random.uniform(20,90)
            ast1 = self.velocity.rotate(angle)
            ast2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            split1 = Asteroid(self.position.x, self.position.y, new_radius)
            split1.velocity = ast1 * ASTEROID_SPEED_INCREASE
            split2 = Asteroid(self.position.x, self.position.y, new_radius)
            split2.velocity = ast2 * ASTEROID_SPEED_INCREASE
        self.kill()
