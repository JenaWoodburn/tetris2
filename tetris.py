# Imports
import pygame
import random
import sys

pygame.init()

# Constant Variables
WIDTH, HEIGHT = (300, 500)
FPS = 35

CELL = 20
ROWS = (HEIGHT - 120) // CELL
COLS = WIDTH // CELL

# Game settings
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Tetris")

# Colours
BLACK = (0,0,0,)
WHITE = (255, 255, 255)
BG_COLOUR = (31, 25, 76)
GRID = (31, 25,132)
WIN = (50, 230, 50)
LOSE = (252, 91, 122)

# Load / Store images
ASSETS = {
    1: pygame.image.load("Assets/1.png"),
    2: pygame.image.load("Assets/2.png"),
    3: pygame.image.load("Assets/3.png"),
    4: pygame.image.load("Assets/4.png")
}

# Fonts
font1 = pygame.font.SysFont("verdana", 50)
font2 = pygame.font.SysFont("verdana", 15)


# Shape Class
class Shape:
    VERSION = {
        'I': [[1, 5, 9, 13], [4, 5, 6, 7]],
        'Z': [[4, 5, 9, 10], [2, 6, 5, 9]],
        'S': [[6, 7, 9, 10], [1, 5, 6, 10]],
        'L': [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        'J': [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        'T': [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        'O': [[1, 2, 5, 6]]
    }
    SHAPES = ['I', 'Z', 'S', 'L', 'J', 'T', 'O']

    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.choice(self.SHAPES)
        self.shape = self.VERSION[self.type]
        self.colour = random.randint(1,4)
        self.orientation = 0

    # Image - choose correct images - version of the shape
    def image(self):
        return self.shape[self.orientation]

    # Rotate
    def rotate(self):
        self.orientation = (self.orientation + 1) % len(self.shape)
 

# Game Class
class Tetris:
    # Constructor
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.score = 0
        self.level = 1
        self.grid = [[0 for i in range(cols)] for j in range(rows)]
        self.next = None
        self.end = False
        self.new_shape()

    # Make grid
    def make_grid(self):
        for i in range(self.rows + 1):
            pygame.draw.line(SCREEN, GRID, (0,CELL*i), (WIDTH, CELL*i))
        for j in range(self.cols + 1):
            pygame.draw.line(SCREEN, GRID, (CELL*j, 0), (CELL*j, HEIGHT-120))

    # Make new shape
    def new_shape(self):
        if not self.next:
            self.next = Shape(5, 0)
        self.figure = self.next
        self.next = Shape(5, 0)

    # Collision detection
    def collision(self) -> bool:
        for i in range(4):
            for j in range(4):
                if (i*4 + j) in self.figure.image():
                    block_row = i + self.figure.y
                    block_col = j + self.figure.x
                    if (block_row >= self.rows or block_col >= self.cols or block_col < 0 or self.grid[block_row][block_col] > 0):
                        return True
        return False

    # Remove row

    # Move down
    def move_down(self):
        self.figure.y += 1
        if self.collision():
            self.figure.y -= 1

    # Move left
    def left(self):
        self.figure.x -= 1
        if self.collision():
            self.figure.x +=  1

    # Move right
    def right(self):
        self.figure.x += 1
        if self.collision():
            self.figure.x -=  1

    # Freefall - when shape is in correct position, freefall lets it drop to bottom of game at once rather than wait for it to fall one row at a time
    def freefall(self):
        while not self.collision():
            self.figure.y += 1
        self.figure.y -= 1

    # Rotate
    def rotate(self):
        orientation = self.figure.orientation
        self.figure.rotate()
        if self.collision():
            self.figure.orientation = orientation



# Main game loop
def main():
    tetris = Tetris(ROWS, COLS)
    counter = 0
    move = True
    run = True
    while run:
        SCREEN.fill(BG_COLOUR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

            keys = pygame.key.get_pressed()
            if not tetris.end:
                if keys[pygame.K_LEFT]:
                    tetris.left()
                elif keys[pygame.K_RIGHT]:
                    tetris.right()
                elif keys[pygame.K_DOWN]:
                    tetris.move_down()
                elif keys[pygame.K_SPACE]:
                    tetris.freefall()
                elif keys[pygame.K_UP]:
                    tetris.rotate()


        # let block fall at constant rate
        counter += 1
        if counter >= 15000:
            counter = 0

        if move:
            if counter % (FPS // (tetris.level*2)) == 0:
                if not tetris.end:
                    tetris.move_down()
                

        tetris.make_grid()

        # show shape on game screen
        if tetris.figure:
            for i in range(4):
                for j in range(4):
                    if (i*4 + j) in tetris.figure.image():
                        shape = ASSETS[tetris.figure.colour]
                        x = CELL * (tetris.figure.x + j)
                        y = CELL * (tetris.figure.y + i)
                        SCREEN.blit(shape, (x,y))
                        pygame.draw.rect(SCREEN, WHITE, (x, y, CELL, CELL), 1)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()