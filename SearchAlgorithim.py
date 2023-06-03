import queue
import pygame

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (220,220,220)
DARK_GRAY = (105,105,105)
GREEN = (0,250,154)
RED = (220,20,60)
BLUE = (135,206,235)
DARK_GREEN = (1, 50, 32)
# currentCell = board.grid[coordinate[0]][coordinate[1]]
#         while(currentCell.color != GREEN):
#             print("BackTracking",currentCell.row,currentCell.col)
#             currentCell.changeToYellow()
#             currentCell = parentGrid[currentCell.row][currentCell.col]
#             pygame.time.delay(1000)

def drawShortestPath(end, parentGrid):
    currentCell = end
    while(currentCell.color != DARK_GREEN):
        print("BackTracking",currentCell.row,currentCell.col)
        if(currentCell.color != RED):
            currentCell.changeToYellow()
        currentCell = parentGrid[currentCell.row][currentCell.col]

def find(board, display):
    grid = board.grid
    board.endFound = False
    q = queue.Queue()
    start = board.start
    cell = grid[start[0]][start[1]]
    q.put(cell)

    parentGrid = []
    for i in range(board.ROW):
        parentGrid.append([])
        for j in range(board.COL):
            parentGrid[i].append([])

    # Continue Searching until end is found, or there is no more path to explore.
    while(not q.empty()):
        cell = q.get()
        if(cell.color == RED):
            #Empty the queue the end is found, no longer need to search
            for i in parentGrid:
                for j in i:
                    if(j):
                        print("(",j.row,j.col,")",end=" ")
                print()
            drawShortestPath(cell,parentGrid)
            while(not q.empty()):
                q.get()
        elif(cell.color == WHITE or cell.color == GREEN):
            #Looking at Neighbors, if they are within the grid
            if(cell.color == WHITE):
                cell.changeToBlue()
            else:
                cell.changeToDarkGreen()
            if(cell.row > 0):
                newCell = grid[cell.row-1][cell.col]
                if(newCell.color != BLUE):
                    parentGrid[cell.row-1][cell.col] = cell
                    q.put(newCell)
            if(cell.row < board.ROW-1):
                newCell = grid[cell.row+1][cell.col]
                if(newCell.color != BLUE):
                    parentGrid[cell.row+1][cell.col] = cell #used for when back tracking to create path
                    q.put(newCell)
            if(cell.col > 0):
                newCell = grid[cell.row][cell.col-1]
                if(newCell.color != BLUE):
                    parentGrid[cell.row][cell.col-1] = cell #used for when back tracking to create path
                    q.put(newCell)
            if(cell.col < board.COL-1):
                newCell = grid[cell.row][cell.col+1]
                if(newCell.color != BLUE):
                    parentGrid[cell.row][cell.col+1] = cell #used for when back tracking to create path
                    q.put(newCell)
            #Update screen when a cell, occurs ever .1 second
            display.drawGrid(board)
            pygame.display.update()
            pygame.time.delay(10)

