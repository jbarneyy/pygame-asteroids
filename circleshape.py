import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):

    def __init__(self, x, y, radius):

        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius


    def draw(self, screen):
        # sub-classes must override
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)


    def update(self, dt):
        # sub-classes must override
        pass


    def detect_collision(self, target):
        
        distance = pygame.Vector2.distance_to(self.position, target.position)
        return distance < (self.radius / 2 + target.radius / 2)
