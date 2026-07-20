import pygame
import circleshape
import shot
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, COLOR, SHOT_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS

# Base class for game objects
class Player(circleshape.CircleShape):
     
    def __init__(self, x: float, y: float) -> None:
          super().__init__(x,y,PLAYER_RADIUS)
          self.rotation = 0
          self.cooldown_timer = 0


    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]  

    def draw(self, screen: pygame.Surface) -> None:
        color = COLOR
        points = self.triangle()
        pygame.draw.polygon(screen, color, points, LINE_WIDTH)

    def rotate(self, dt) -> None:
         self.rotation += dt*PLAYER_TURN_SPEED
    
    def move(self, dt) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def update(self, dt: float) -> None:
        self.cooldown_timer -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
        

    def shoot(self):
        if (self.cooldown_timer > 0): 
            pass
        else: 
            unit_vector = pygame.Vector2(0, 1).rotate(self.rotation)
            fire = shot.Shot(self.position.x, self.position.y , SHOT_RADIUS)
            fire.velocity = unit_vector*PLAYER_SHOOT_SPEED 
            self.cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS