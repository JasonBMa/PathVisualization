'''
Board Class, used to keep track of the current grid layout,
mainly used so we can do algorithims on
is updated every frame 1/60 of a second
'''
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (220,220,220)
DARK_GRAY = (105,105,105)
GREEN = (0,250,154)
RED = (220,20,60)
BLUE = (135,206,235)
YELLOW = (240,230,140)
DARK_GREEN = (1, 50, 32)
class Cell:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def changeToBlue(self):
        self.color = BLUE

    def changeToYellow(self):
        self.color = YELLOW

    def changeColor(self, color):
        self.color = color

    def changeToDarkGreen(self):
        self.color = DARK_GREEN

class Board:
    def __init__(self, col, row, cellDensity):
        self.ROW = row*cellDensity
        self.COL = col*cellDensity
        self.grid = []
        for i in range(self.ROW):
            self.grid.append([])
            for j in range(self.COL):
                cell = Cell(i,j,WHITE)
                self.grid[i].append(cell)

        self.start=[0,0]
        cell = self.grid[0][0]
        cell.color = GREEN
        cell = self.grid[self.ROW-1][self.COL-1]
        cell.color = RED
        self.endFound = False

    def loadBoard(self, updatedGrid):
        self.grid = updatedGrid

    def updateCell(self,row,col):
        cell = self.grid[row][col]
        if (cell.color == WHITE): # gray to dark gray
            cell.color = LIGHT_GRAY
        elif (cell.color == LIGHT_GRAY): # dark gray to gray
            cell.color = WHITE