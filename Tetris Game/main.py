### Tetris ###

import pygame, sys 
import random
from grid import Grid

pygame.init()
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris by Riot09")
clock = pygame.time.Clock()

game_grid = Grid()
game_grid.print_grid()

#pygame.mixer.init(frequency=16000)
#pygame.mixer.music.load("./Tetris Game/tetris.mp3")
#pygame.mixer.music.play(loops=2)

while pygame.mixer.music.get_busy() == True:
        continue

while True:
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()
            running = False
    pygame.display.update()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    game_grid.draw(screen)

    # RENDER YOUR GAME HERE
    
    # flip() the display to put your work on screen
    pygame.display.flip()
    

    clock.tick(60)  # limits FPS to 60



pygame.quit()