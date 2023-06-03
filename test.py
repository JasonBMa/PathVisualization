import pygame

# Initialize Pygame
pygame.init()

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up the initial size of the board
CELL_SIZE = 50
ROWS = 8
COLS = 8

# Set up the dimensions of the board based on initial size and cell density
WIDTH = CELL_SIZE * COLS
HEIGHT = CELL_SIZE * ROWS

# Initialize the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Board")

# Create the game board
board = [[0] * COLS for _ in range(ROWS)]

# Function to update the board
def update_board(row, col):
    board[row][col] = (board[row][col] + 1) % 2

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            pos = pygame.mouse.get_pos()
            # Convert the mouse position to board coordinates
            col = pos[0] // CELL_SIZE
            row = pos[1] // CELL_SIZE
            # Update the board
            update_board(row, col)
        elif event.type == pygame.KEYDOWN:
            # Scale up the board on '+' key press
            if event.key == pygame.up or event.key == pygame.K_KP_PLUS:
                CELL_SIZE += 10
                ROWS = HEIGHT // CELL_SIZE
                COLS = WIDTH // CELL_SIZE
                board = [[0] * COLS for _ in range(ROWS)]
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
            # Scale down the board on '-' key press
            elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                if CELL_SIZE > 10:
                    CELL_SIZE -= 10
                    ROWS = HEIGHT // CELL_SIZE
                    COLS = WIDTH // CELL_SIZE
                    board = [[0] * COLS for _ in range(ROWS)]
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Fill the screen with white color
    screen.fill(WHITE)

    # Draw the cells
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 1:
                color = BLUE
            else:
                color = BLACK
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()