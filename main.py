import pygame # type: ignore
from constants import *
from player import Player


def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    # init player class in the middle of the screen
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

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
                print("Closing Ateroids.")
                return
            
        # fills the screen black and draws player
        pygame.Surface.fill(screen,(0,0,0))
        player.draw(screen)
        player.update(dt)

        # refreshes the screen, sets it to 60fps, sets dt(time from last refresh) to seconds
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
 