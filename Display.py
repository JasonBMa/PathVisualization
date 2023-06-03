import pygame

'''
Display Class:
Controls the display of the user, from creating graphics
and some basic validations.
'''

#Colors for Graphics
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (220,220,220)
DARK_GRAY = (105,105,105)
GREEN = (0,250,154)
RED = (220,20,60)
BLUE = (135,206,235)


class Display:
    def __init__(self,height,width,CELL_SIZE):
        pygame.init()
        pygame.display.set_caption('Path Visualizer')
        self.height = height
        self.width = width
        self.offsetX = 30
        self.offsetY = 30
        self.screen = pygame.display.set_mode((width,height))
        self.screen.fill(DARK_GRAY)
        self.CELL_SIZE = CELL_SIZE

    def setup(self):
        pygame.init()
        pygame.display.set_caption('Path Visualizer')
        self.screen.fill(LIGHT_GRAY)

    def drawGrid(self,board):
        grid = board.grid
        for row in range(board.ROW):
            for col in range(board.COL):
                cell = grid[row][col]
                pygame.draw.rect(self.screen, cell.color, (col * self.CELL_SIZE + self.offsetX, row * self.CELL_SIZE + self.offsetY, self.CELL_SIZE, self.CELL_SIZE))

    def pygameWait(amt):
        pygame.time.wait(amt)

    def render():
        pygame.display.update()

    def validPosition(self,boardRow,boardCol,pos):
        #Checks if x position is within grid
        if(self.offsetX > pos[0] or pos[0] > (self.offsetX+(boardCol*self.CELL_SIZE))):
                print("Invalid Position, nothing done")
                return False

        #Checks if Y position is within grid
        if(self.offsetY > pos[1] or pos[1] > (self.offsetY+(boardRow*self.CELL_SIZE))):
                print("Invalid Position, nothing done")
                return False
        return True