import pygame # type: ignore
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    asteroid_field = AsteroidField()

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
    
        updateable.update(dt)
        # fills the screen black and draws player
        screen.fill("black")
        for i in drawable:
            i.draw(screen)


        # refreshes the screen, sets it to 60fps, sets dt(time from last refresh) to seconds
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
 