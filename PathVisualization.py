import pygame
import sys
import math
from sys import exit
from Board import Board
from Display import Display

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (220,220,220)
DARK_GRAY = (105,105,105)
GREEN = (0,250,154)
RED = (220,20,60)
BLUE = (135,206,235)

ratio = [4,3] # Used to scale the UI
size = 300 #Recommended size 80 - 100
CELL_SIZE = 80
width = ratio[0] * size
height = ratio[1] * size

clock = pygame.time.Clock()
'''
Board Class, used to keep track of the current grid layout,
mainly used so we can do algorithims on
is updated every frame 1/60 of a second
'''
board = Board(ratio[0]*3,ratio[1]*3)
display = Display(height,width)
board.printBoard()
running = True
while running:
    #Recieve user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            pos = pygame.mouse.get_pos()
            # Convert the mouse position to board coordinates

            display.validPosition(ratio,pos)

            col = (pos[0] - display.offsetX) // CELL_SIZE
            row = (pos[1] - display.offsetY) // CELL_SIZE

            # print("(",col,",",row,")", "grid coordinate")
            # Update the board
            board.updateCell(row, col)
        elif event.type == pygame.K_SPACE:
            print("Begin Search")
            #Sort Algorithim
    #Print out the updated grid at the end, should occur 60 times a second creating a 60 fps display.
    display.drawGrid(board)
    pygame.display.update()
    clock.tick(60)


pygame.quit()
exit()