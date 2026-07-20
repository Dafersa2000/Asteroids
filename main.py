import pygame
from logger import log_state, log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import player
import shot
import asteroid
import asteroidfield
import sys

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    shot.Shot.containers = (shots, updatable, drawable)
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids,updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    field = asteroidfield.AsteroidField()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    figure = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        log_state()
        updatable.update(dt)
        for meteor in asteroids:
            if meteor.collides_with(figure):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
            for fire in shots:
                if meteor.collides_with(fire):
                    log_event("asteroid_shot")
                    meteor.split()
                    fire.kill()
        screen.fill(color = (0,0,0))
        for drawing in drawable: 
            drawing.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60)/1000
        pygame.display.flip()



if __name__ == "__main__":
    print(rf" Running pygame version  {pygame.version.ver}")
    main()
