import pygame
import player
from constants import *

def main():
    print("Starting Asteroids!")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    PLAYER = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    game_clock = pygame.time.Clock()
    dt = 0


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # On each game loop: Fill screen obj with black background. Call player obj to draw itself to screen.
        
        SCREEN.fill("black")

        PLAYER.update(dt)
        PLAYER.draw(SCREEN)
        



        # Pygame/Display module method for refreshing screen.
        pygame.display.flip()

        # Pauses game from refreshing for 1/60th of a second. dt stores time in seconds from last refresh.
        dt = game_clock.tick(60) / 1000
        





if __name__ == "__main__":
    main()
