from circleshape import CircleShape
import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED

class Player(CircleShape):
    def __init__(self, x, y, radius=PLAYER_RADIUS):     

        super().__init__(x, y, radius)

        self.position = pygame.math.Vector2(x,y)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        # Update the missing lines to call the rotate method with the dt argument. To go left instead of right when a is pressed, 
        # you'll need to invert dt... how can you do that...?
        if keys[pygame.K_a]:
            # inverted dt = -dt            
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)