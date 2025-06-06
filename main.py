import pygame
import player
import asteroid as ast
import asteroidfield
import shot
import sys
from constants import *


updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()


def main():
    print("Starting Asteroids!")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()


    asteroidfield.AsteroidField.containers = (updatable)
    ast.Asteroid.containers = (updatable, drawable, asteroids)
    player.Player.containers = (updatable, drawable)
    shot.Shot.containers = (updatable, drawable, shots)

    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    PLAYER = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)
    ASTEROIDFIELD = asteroidfield.AsteroidField()

    game_clock = pygame.time.Clock()
    dt = 0


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # On each game loop: Fill screen obj with black background. Call player obj to draw itself to screen.
        
        SCREEN.fill("black")

        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(SCREEN)
        
        for asteroid in asteroids:
            if asteroid.detect_collision(PLAYER):
                print("Game over!")
                sys.exit()


        # Pygame/Display module method for refreshing screen.
        pygame.display.flip()

        # Pauses game from refreshing for 1/60th of a second. dt stores time in seconds from last refresh.
        dt = game_clock.tick(60) / 1000
        





if __name__ == "__main__":
    main()
