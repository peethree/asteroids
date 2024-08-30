from circleshape import CircleShape
from constants import *
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)        

    def draw(self, screen):
        # Override the draw() method to draw the asteroid as a pygame.draw.circle. 
        # Use its position, radius, and a width of 2
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # Override the update() method so that it moves in a straight line at constant speed. 
        # On each frame, it should add (velocity * dt) to its position.        
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        # small asteroid (just destroy it and do nothing)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return        

        # random angle between 20, 50
        random_angle = random.uniform(20, 50)

        # Use the rotate method on the asteroid's velocity vector to create 2 new vectors, 
        # that are rotated by random_angle and -random_angle respectively (they should split in opposite directions).
        pos_rotate = self.velocity.rotate(random_angle)
        neg_rotate = self.velocity.rotate(-random_angle)

        # old_radius - ASTEROID_MIN_RADIUS
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two new Asteroid objects at the current asteroid position with the new radius.
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Set the first's velocity to the first new vector, but make it move faster by scaling it up (multiplying) by 1.2
        asteroid1.velocity = pos_rotate * 1.2
        # same for second, with 2nd vector
        asteroid2.velocity = neg_rotate * 1.2