import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    print("Starting Asteroids")
    print(rf"Screen width: {SCREEN_WIDTH}")
    print(rf"Screen height: {SCREEN_HEIGHT}")
    while True:
        log_state()
        screen.fill(color = (0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()



if __name__ == "__main__":
    print(rf" Running pygame version  {pygame.version.ver}")
    main()
