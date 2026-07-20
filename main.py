import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import player

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    figure = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        log_state()
        updatable.update(dt)
        screen.fill(color = (0,0,0))
        for drawing in drawable: 
            print(drawing)
            drawing.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60)/1000
        pygame.display.flip()
        print(dt)



if __name__ == "__main__":
    print(rf" Running pygame version  {pygame.version.ver}")
    main()
