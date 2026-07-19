import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    print("Starting Asteroids")
    print(rf"Screen width: {SCREEN_WIDTH}")
    print(rf"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    print(rf" Running pygame version  {pygame.version.ver}")
    main()
