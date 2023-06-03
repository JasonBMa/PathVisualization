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

class Cell:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def changeToBlue(self):
        self.color = BLUE

    def changeColor(self, color):
        self.color = color

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
        cell = self.grid[row-1][col-1]
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