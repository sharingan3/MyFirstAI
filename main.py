import pygame
import sys
import random
from time import sleep

all_obstacle_pos = [[], []]
all_free_space = [(i, j) for i in range(20, 420, 20) for j in range(20, 420, 20)]

############################################Snake

"Define the snakes methods and attributes"
class Snake():
    def __init__(self):
        self.length = 1
        self.positions = [((40), (40))]
        self.direction = right
        self.color = (17, 24, 47)
        self.crashed = False
        self.score = 0

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * - 1, point[1] * - 1) == self.direction:
            pass
        
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * gridsize)) % screen_width), (cur[1] + (y * gridsize)) % screen_height)

        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()

        else:
            if self.crashed == False: 
                self.positions.insert(0, new)
                if len(self.positions) > self.length:
                    self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [(40, 40)]
        self.direction = random.choice([up, down, left, right])
        self.score = 0

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridsize,gridsize))

            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93, 216, 228), r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    "Here is the ai that I try to make without a*"
    def ai(self, start, end):
        x_diff = 0
        y_diff = 0

        if start[0] > end[0]:
            x_diff = -(start[0] - end[0])

        elif start[0] < end[0]:
            x_diff = end[0] - start[0]

        if start[1] > end[1]:
            y_diff = -(start[1] - end[1])

        elif start[1] < end[1]:
            y_diff = end[1] - start[1]

        "See which direction to go"

        if y_diff > 0:
            for y in range(int(y_diff)):
                self.turn(down)

        elif y_diff < 0:
            y_diff = abs(y_diff)
            for y in range(int(y_diff)):
                self.turn(up) 

        if x_diff > 0:
            for x in range(int(x_diff)):
                self.turn(right)

        elif x_diff < 0:
            x_diff = abs(x_diff)
            for x in range(int(x_diff)):
                self.turn(left)

################################################Food

"Create food's attributes and methods"
class Food():
    def __init__(self, the_wall, the_snake):
        self.limit = the_wall
        self.the_snake_body = the_snake
        self.position = (0, 0)
        self.color = (223, 163, 49)
        
        for i in self.limit:
            if i in all_free_space:
                all_free_space.remove(j)
        
        for j in self.the_snake_body:
            if j in all_free_space:
                all_free_space.remove(j)

        self.randomize_position()

    def randomize_position(self):
        self.position = (random.choice(all_free_space))

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)

#################################Create grid(not necessary though)

"Draw the grid"
def drawGrid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x * gridsize, y * gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface, (93,216,228), r)
            else:
                rr = pygame.Rect((x * gridsize, y * gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface, (84,194,205), rr)

##############################################Create the wall

"Draw wall"

class WallCell():
    def __init__(self):            
        self.position = (0, 0)
        self.color = (222, 52, 235)

    def create_cell(self, surface, side, index):
        if side == "up":
            pygame.draw.rect(surface, (222, 52, 235), [index, 0, 20, 20])
            self.position = (index, 0)
            all_obstacle_pos[1].append(self.position)
        
        elif side == "down":
            pygame.draw.rect(surface, (222, 52, 235), [index, 460, 20, 20])
            self.position = (460, index)
            all_obstacle_pos[1].append(self.position)

        elif side == "left":
            pygame.draw.rect(surface, (222, 52, 235), [0, index, 20, 20])
            self.position = (0, index)
            all_obstacle_pos[1].append(self.position)

        elif side == "right":
            pygame.draw.rect(surface, (222, 52, 235), [460, index, 20, 20])
            self.position = (index, 460)
            all_obstacle_pos[1].append(self.position)

################################Create dimensions of the window and magnitude of turn

screen_width = 480
screen_height = 480

gridsize = 20
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

#######################################Start game loop

"The game loop"
def main():
    pygame.init()

    "Set up the screen"
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    "Make instance of wall"
    wall_cell = WallCell()

    "Define the surface where the snake, apple, wall cells will be placed"
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    
    "Draw the grid"
    drawGrid(surface)

    "Create instance of snake and apple"
    snake = Snake()
    food = Food(all_obstacle_pos, snake.positions)

    "Define the scores font"
    myfont = pygame.font.SysFont("monospace", 16)

    "Begin the game loop"
    running = True

    while running:
        "Set fps, detect key events, draw grid a second time and make the snake move forward"
        clock.tick(10)
        snake.handle_keys()
        drawGrid(surface)
        snake.move()
        snake.ai(snake.get_head_position(), food.position)

        for i in snake.positions[0]:
            if i not in all_obstacle_pos[0]:
                all_obstacle_pos[0].append(i)
    
        "Use loop to draw the walls"
        for i in range(0, 481, 20):
            wall_cell.create_cell(surface, "up", i)
    
        for j in range(0, 481, 20):        
            wall_cell.create_cell(surface, "left", j)

        for ix in range(0, 481, 20):
            wall_cell.create_cell(surface, "down", ix)

        for jy in range(0, 481, 20):  
            wall_cell.create_cell(surface, "right", jy)

        "Detect if the snake's head is in the same location as the apple"
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position()

        "Redraw everything to ypdate the screen"
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0,0))
        
        "Make the game over text"
        game_over_font = pygame.font.SysFont('Bowlby One SC', 24)
        textsurface = game_over_font.render('GAME OVER', False, (0, 0, 0))

        "Check if crashed"
        for item in all_obstacle_pos:
            for snake_pos in all_obstacle_pos[0]:
                if snake.positions[0] == snake_pos:
                    screen.blit(textsurface, (175, 200))
                    #The below one is for a loop
                    snake.reset()
                    #The below one is for arcade mode
                    #running = False

            for wall_pos in all_obstacle_pos[1]:
                if snake.positions[0] == wall_pos:
                    screen.blit(textsurface, (175, 200))
                    snake.reset()         

        "Draw the score on the top left corner"
        text = myfont.render("Score {0}".format(snake.score), 1, (0,0,0))
        screen.blit(text, (5,3))
        pygame.display.update()

    print(snake.score)
    sleep(3)

#################Run main if this is the file that was runned 
if __name__ == "__main__":
    main()
