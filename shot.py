import pygame
import circleshape
from constants import COLOR, LINE_WIDTH, SHOT_RADIUS

class Shot(circleshape.CircleShape):
    
    def __init__(self, x:float, y:float, radius:float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, COLOR, self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt