class Board:
    def __init__(self, col, row):
        self.ROW = row
        self.COL = col
        self.grid = [[0 for x in range(col)]for y in range(row)]
        self.grid[0][0] = 1

    def printBoard(self):
        for i in range(self.ROW):
            for j in range(self.COL):
                print(self.grid[i][j] ,end=" ")

            print()

    def loadBoard(self, updatedGrid):
        self.grid = updatedGrid

    def updateCell(self,row,col):
        if (self.grid[row][col] == 0): # gray to dark gray
            self.grid[row][col] = 1
        elif (self.grid[row][col] == 1): # dark gray to gray
            self.grid[row][col] = 0