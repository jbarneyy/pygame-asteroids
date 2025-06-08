import circleshape
import pygame
import random
from constants import *

class Stars():

    def __init__(self):
        self.current_stars = []

        for _ in range(0, MAX_STARS):
            self.current_stars.append(circleshape.CircleShape(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), 1))

    
    def draw(self, screen):
        for star in self.current_stars:
            pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        pass
        
