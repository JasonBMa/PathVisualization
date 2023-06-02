import queue

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (220,220,220)
DARK_GRAY = (105,105,105)
GREEN = (0,250,154)
RED = (220,20,60)
BLUE = (135,206,235)

def find(board):
    print("Beginning Search for End")
    grid = board.grid
    board.endFound = False
    q = queue.Queue()
    start = board.start
    cell = grid[start[0]][start[1]]
    q.put(cell)

    # Continue Searching until end is found, or there is no more path to explore.
    while(not q.empty()):
        cell = q.get()
        if(cell.color == RED):
            #Empty the queue the end is found, no longer need to search
            while(not q.empty()):
                q.get()
        if(cell.color == WHITE or cell.color == GREEN):
            #Looking at Neighbors, if they are within the grid
            if(cell.color == WHITE):
                cell.changeToBlue()
            if(cell.row > 0):
                newCell = grid[cell.row-1][cell.col]
                q.put(newCell)
            if(cell.row < board.ROW-1):
                newCell = grid[cell.row+1][cell.col]
                q.put(newCell)
            if(cell.col > 0):
                newCell = grid[cell.row][cell.col-1]
                q.put(newCell)
            if(cell.col < board.COL-1):
                newCell = grid[cell.row][cell.col+1]
                q.put(newCell)