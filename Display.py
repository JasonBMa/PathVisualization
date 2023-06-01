import pygame
#Colors for Graphics
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (220,220,220)
DARK_GRAY = (105,105,105)
GREEN = (0,250,154)
RED = (220,20,60)
BLUE = (135,206,235)

CELL_SIZE = 80 ## Size of each Cell, becomes ex. 80 by 80 px cell.

class Display:
    def __init__(self,height,width):
        pygame.init()
        pygame.display.set_caption('Path Visualizer')
        self.height = height
        self.width = width
        self.offsetX = 30
        self.offsetY = 30
        self.screen = pygame.display.set_mode((width,height))
        self.screen.fill(LIGHT_GRAY)

    def setup(self):
        pygame.init()
        pygame.display.set_caption('Path Visualizer')
        self.screen.fill(LIGHT_GRAY)

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
                pygame.draw.rect(self.screen, Display.getColor(grid[row][col]), (col * CELL_SIZE + self.offsetX, row * CELL_SIZE + self.offsetY, CELL_SIZE, CELL_SIZE))

    def returnGrid():
        grid = None
        return grid

    def render():
        pygame.display.update()

    def validPosition(self,ratio,pos):
        #Checks if x position is within grid
        if(self.offsetX > pos[0] or pos[0] > (self.offsetX+(ratio[0]*CELL_SIZE*3))):
                print("Invalid Position, nothing done")
                return False
        #Checks if Y position is within grid
        if(self.offsetY > pos[1] or pos[1] > (self.offsetY+(ratio[1]*CELL_SIZE*3))):
                print("Invalid Position, nothing done")
                return False
        return True