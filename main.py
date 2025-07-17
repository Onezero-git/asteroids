import pygame # type: ignore
import sys
import time
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    kills = 0
    start = time.time()
    player_life = 3
    player_invincibility = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    Shot.containers = (shots, updateable, drawable)
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
        player_invincibility -= 0.016
        
        # Collision detection: player with asteroids -> game overa
        for asteroid in asteroids:
            if asteroid.collision(player) and player_invincibility <= 0:
                if player_life > 0:
                    player_life -= 1
                    player.position = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
                    player_invincibility = 2
                else:
                    print("Game over!")
                    end = time.time()
                    length = end - start
                    if kills == 1:
                        print(f"You survived for {int(length)} seconds!")
                        print(f"You have destroyed {kills} asteroid!")
                    else:
                        print(f"You have played for {int(length)} seconds!")
                        print(f"You have destroyed {kills} asteroids!")
                    sys.exit()

        # Collision detection: shot with asteroids -> destroy both
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.split(shot)
                    kills += 1

        # fills the screen black and draws player
        screen.fill("black")
        for i in drawable:
            i.draw(screen)


        # refreshes the screen, sets it to 60fps, sets dt(time from last refresh) to seconds
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
 