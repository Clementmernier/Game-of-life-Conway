import pygame
import sys
import time


BLACK = (255, 255, 255)
WHITE = (0,0,0)
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
cell_size = 10
cols, rows = WINDOW_WIDTH // cell_size, WINDOW_HEIGHT // cell_size
PLAYING = False  


grid = [[0 for _ in range(cols)] for _ in range(rows)]


pygame.display.set_caption("Jeu de la Vie")


def draw_grid():
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            color = WHITE if grid[row][col] == 0 else BLACK
            pygame.draw.rect(SCREEN, color, rect, 0)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)
def handle_click(pos):
    x, y = pos
    col = x // cell_size
    row = y // cell_size
   
    grid[row][col] = 1 if grid[row][col] == 0 else 0


def count_neighbors(x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            nx, ny = x + i, y + j
            if 0 <= nx < rows and 0 <= ny < cols:
                count += grid[nx][ny]
    return count

# Fonction pour mettre à jour l'état de la grille
def update_grid():
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for x in range(rows):
        for y in range(cols):
            neighbors = count_neighbors(x, y)
            if grid[x][y] == 1:
                
                if neighbors == 2 or neighbors == 3:
                    new_grid[x][y] = 1
            else:
                
                if neighbors == 3:
                    new_grid[x][y] = 1
    return new_grid


def main():
    global SCREEN, CLOCK, PLAYING, grid
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH+200, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()

    last_update = time.time()

    while True: 
        SCREEN.fill(WHITE)
        draw_grid()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_click(pygame.mouse.get_pos())
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    PLAYING = not PLAYING  

        
        if PLAYING and time.time() - last_update > 0.5:
            grid = update_grid()
            last_update = time.time()

        pygame.display.flip()
        CLOCK.tick(60)  

main()
