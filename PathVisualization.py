import pygame
from sys import exit
from Board import Board
from Display import Display
import SearchAlgorithim
from threading import Thread

ratio = [4,3] # Used to scale the UI
size = 300 #Recommended size 80 - 100
CELL_SIZE = 80
width = ratio[0] * size
height = ratio[1] * size
frameRate = 60
# Clock used for refresh rate of the display
clock = pygame.time.Clock()

board = Board(ratio[0]*3,ratio[1]*3)
display = Display(height,width)
running = True
while running:
    #Recieve user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif (event.type == pygame.MOUSEBUTTONDOWN):
            # Get the mouse position
            pos = pygame.mouse.get_pos()
            #Check if mouse position is in the grid
            if (display.validPosition(ratio,pos) == False): #stops out of bound accesses
                continue

            # Convert the mouse position to board coordinates
            col = (pos[0] - display.offsetX) // CELL_SIZE
            row = (pos[1] - display.offsetY) // CELL_SIZE

            # Update the board
            board.updateCell(row, col)

        elif (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_SPACE):
                #Search Algorithim
                frameRate = 5
                SearchAlgorithim.find(board,display)

    #Print out the updated grid at the end, should occur 60 times a second creating a 60 fps display.
    display.drawGrid(board)
    pygame.display.update()
pygame.quit()
exit()