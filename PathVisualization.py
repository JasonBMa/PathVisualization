import pygame
from sys import exit
from Board import Board
from Display import Display
import SearchAlgorithim

ratio = [4,3] # Used to scale the UI
cellDensity = 10 # Controls how many cells within the screen
size = 300 #Recommended size 200
CELL_SIZE = size*2//3 // cellDensity
width = ratio[0] * size
height = ratio[1] * size

# Clock used for refresh rate of the display
clock = pygame.time.Clock()
board = Board(ratio[0],ratio[1],cellDensity)
display = Display(height,width,CELL_SIZE)

running = True
while running:
    #Recieve user input
    pygame.event.pump() #Just to stop freezing as OS will think program is not being used and will get yielded for other applications
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif (pygame.mouse.get_pressed()[0]):
            # Get the mouse position
            pos = pygame.mouse.get_pos()
            #Check if mouse position is in the grid
            if (display.validPosition(board.ROW,board.COL,pos) == False): #stops out of bound accesses
                continue

            # Convert the mouse position to board coordinates
            col = (pos[0] - display.offsetX) // CELL_SIZE
            row = (pos[1] - display.offsetY) // CELL_SIZE
            # Update the board
            board.createWall(row, col)

        elif (pygame.mouse.get_pressed()[2]):
            # Get the mouse position
            pos = pygame.mouse.get_pos()
            #Check if mouse position is in the grid
            if (display.validPosition(board.ROW,board.COL,pos) == False): #stops out of bound accesses
                continue

            # Convert the mouse position to board coordinates
            col = (pos[0] - display.offsetX) // CELL_SIZE
            row = (pos[1] - display.offsetY) // CELL_SIZE
            # Update the board
            board.deleteWall(row, col)

        elif (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_SPACE):
                if(board.endFound == True):
                    board = Board(ratio[0],ratio[1],cellDensity)
                    continue

                #Search Algorithim
                SearchAlgorithim.find(board,display)


    #Print out the updated grid at the end, should occur 60 times a second creating a 60 fps display.
    display.drawGrid(board)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
exit()