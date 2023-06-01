import pygame
import sys
import math
from sys import exit
from Board import Board


# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (220,220,220)
DARK_GRAY = (105,105,105)
GREEN = (0,250,154)
RED = (220,20,60)
BLUE = (135,206,235)
#draw all our elements
    #update everything
ratio = [4,3] # Used to scale the UI
size = 200 #Recommended size 80 - 100
CELL_SIZE = 10
width = ratio[0] * size
height = ratio[1] * size
pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Path Visualizer')
clock = pygame.time.Clock()
'''
Board Class, used to keep track of the current grid layout,
mainly used so we can do algorithims on
is updated every frame 1/60 of a second
'''

class Display:
    def __init__(self,height,width):
        self.height = height
        self.width = width
        self.offsetX = 30
        self.offsetY = 30

    def setup():
        screen.fill(LIGHT_GRAY)

    def getColor(value):
        if(value == 0):
            return WHITE
        elif(value == 1):
            return DARK_GRAY
        elif(value == 2):
            return BLUE
        elif(value == 3):
            return GREEN
        elif(value == 4):
            return RED

    def drawGrid(self,board):
        grid = board.grid
        for row in range(board.ROW):
            for col in range(board.COL):
                pygame.draw.rect(screen, Display.getColor(grid[row][col]), (col * CELL_SIZE + self.offsetX, row * CELL_SIZE + self.offsetY, CELL_SIZE, CELL_SIZE),3)

    def returnGrid():
        grid = None
        return grid



board = Board(ratio[0],ratio[1])
display = Display(height,width)
Display.setup()
board.printBoard()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            pos = pygame.mouse.get_pos()
            # Convert the mouse position to board coordinates
            print(pos, "grabbed from cursor")
            print("Limit for X Coordinate of the Cursor is between", display.offsetX,"and",display.offsetX+(ratio[0]*size))
            print("Limit for Y Coordinate of the Cursor is between", display.offsetY,"and",display.offsetY+(ratio[1]*size))
            print(pos)
            # if(display.offsetX < pos[0] and pos[0] <= (display.offsetX+(ratio[0]*size))):
            #     print("Not Valid")
            #     continue

            # if(display.offsetY < pos[1] and pos[1] <= (display.offsetY+(ratio[1]*size))):
            #     print("Not Valid")
            #     continue

            col = (pos[0] - display.offsetX) // CELL_SIZE
            row = (pos[1] - display.offsetY) // CELL_SIZE

            #print("(",col,",",row,")", "grid coordinate")
            # Update the board
            board.updateCell(row, col)
        elif event.type == pygame.K_SPACE:
            print("Begin Search")
            #Sort Algorithim

    display.drawGrid(board)
    pygame.display.update()
    clock.tick(60)


pygame.quit()
exit()