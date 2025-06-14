import pygame
import circleshape
from constants import *
import shot
from main import shots

class Player(circleshape.CircleShape):
    
    
    def __init__(self, x, y, shots):
        super().__init__(x, y, PLAYER_RADIUS)
        
        self.shots = shots
        self.rotation = 0

        self.timer = 0

    

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]



    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        

    def rotate(self, dt):
        self.rotation = self.rotation + (PLAYER_TURN_SPEED * dt)

    
    def update(self, dt):
        self.timer -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
            self.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        if keys[pygame.K_s]:
            self.move(dt * -1)
            self.velocity = pygame.Vector2(0, -1).rotate(self.rotation)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.position += self.velocity


        # For wrapping player to opposite side when going off screen.
        if (self.position.x >= SCREEN_WIDTH):
            self.position.x = 0.01
        if (self.position.x <= 0):
            self.position.x = SCREEN_WIDTH - 0.01

        if (self.position.y >= SCREEN_HEIGHT):
            self.position.y = 0.01
        if (self.position.y <= 0):
            self.position.y = SCREEN_HEIGHT - 0.01
            
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


    def shoot(self):

        if (self.timer <= 0):
            self.timer = PLAYER_SHOOT_COOLDOWN

            pewpew = shot.Shot(self.position.x, self.position.y, SHOT_RADIUS)
            pewpew.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shots.add(pewpew)

        









        