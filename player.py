from circleshape import CircleShape
import pygame
from constants import PLAYER_SHOOT_COOLDOWN, PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y, radius=PLAYER_RADIUS):     

        super().__init__(x, y, radius)

        self.position = pygame.math.Vector2(x,y)
        self.rotation = 0
        self.timer = 0

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
        self.timer -= dt
        keys = pygame.key.get_pressed()

        # Update the missing lines to call the rotate method with the dt argument. To go left instead of right when a is pressed, 
        # you'll need to invert dt... how can you do that...?
        if keys[pygame.K_a]:
            # inverted dt = -dt            
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
            

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):       
        if self.timer > 0:
            return         
        
        shot = Shot(self.position.x, self.position.y)
        starting_vector = pygame.math.Vector2(0,1)
        shot.velocity = starting_vector.rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN