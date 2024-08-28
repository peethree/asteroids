import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroidfield = AsteroidField()

    # Use an infinte while loop for the game loop. At each iteration, it should:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        
        delta_time = clock.tick(60)
        dt = delta_time / 1000

        for item in updatable:
            item.update(dt)
            
        screen.fill("black")

        for item in drawable:
            item.draw(screen)

        
        # player.draw(screen)

        # Use the screen's fill method to fill the screen with a solid "black" color.
        # Use pygame's display.flip() method to refresh the screen.
        pygame.display.flip()


       

        # player.update(dt)



if __name__ == "__main__":
    main()