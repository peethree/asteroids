import pygame
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Use an infinte while loop for the game loop. At each iteration, it should:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        # Use the screen's fill method to fill the screen with a solid "black" color.
        # Use pygame's display.flip() method to refresh the screen.
        pygame.display.flip()



if __name__ == "__main__":
    main()