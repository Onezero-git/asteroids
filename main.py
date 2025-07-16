import pygame
from constants import *
def main():
    pygame.init()

    # New GUI Window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Infinite Game loop
    while True:
        # Make the "X" button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        pygame.display.flip()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
