import pygame
import sys
import math
from sys import exit


#draw all our elements
    #update everything
height = 1000
width = 1500
pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Path Visualizer')
clock = pygame.time.Clock()
'''
Board Class, used to keep track of the current grid layout,
mainly used so we can do algorithims on
is updated every frame 1/60 of a second
'''
class Board:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.grid = [[0]*col]*row

    def printBoard(self):
        for i in range(0,self.row):
            print(self.grid[i])

    def loadBoard(self, updatedGrid):
        self.grid = updatedGrid

class Display:
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def drawGrid(grid):
        return
        #code

    def returnGrid():
        grid = None
        return grid

    def updateCell(row,col):
        if (Board.grid[row][col] == 0): # gray to dark gray
            Board.grid[row][col] = 1
        elif (Board.grid[row][col] == 1): # dark gray to gray
            Board.grid[row][col] = 0


board = Board(5,6)
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
            col = pos[0] #CELL_SIZE
            row = pos[1] #CELL_SIZE

            # Update the board
            board.updateCell(row, col)
            exit()
        elif event.type == pygame.K_SPACE:
            print("Begin Search")
            #Sort Algorithim

    pygame.display.update()
    clock.tick(60)


pygame.quit()
exit()