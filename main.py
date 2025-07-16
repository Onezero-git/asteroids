import pygame # type: ignore
from constants import *


def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    # New GUI Window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Infinite Game loop
    while True:
        # Make the "X" button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(dt)
                print("Closing Ateroids.")
                return
            
        # fills the screen black
        pygame.Surface.fill(screen,(0,0,0))
        # refreshes the screen
        pygame.display.flip()
        # sets the fps to 60
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
 