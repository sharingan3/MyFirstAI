import sys
import pygame
import random
from grid import up, down, left, right, maze
from grid import gridsize, screen_width, screen_height

def square_drawer(cube, surface):
    the_cube_visualization = pygame.Rect(cube[0] * 20, cube[1] * 20, gridsize, gridsize)
    pygame.draw.rect(surface, (255, 0, 0), the_cube_visualization, 3)

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(40, 40)] # All of the positions of the snake's body
        self.direction = down
        self.color = (0, 168, 28)
        self.crashed = False
        self.score = 0

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if (point[0], point[1]) != self.direction:
            self.direction = point
        
        else:
            pass

    def move(self):
        self.cur = self.get_head_position()
        self.turn(self.direction)
        self.x, self.y = self.direction 

        self.new = (((self.cur[0] + (self.x * gridsize)) % screen_width), (self.cur[1] + (self.y * gridsize)) % screen_height)

        if len(self.positions) > 2 and self.new in self.positions[2:]:
            self.reset()

        else:
            if self.crashed == False:
                self.positions.insert(0, self.new)
                if len(self.positions) > self.length:
                    self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [(40, 40)]
        self.direction = random.choice([up, down, left, right])
        self.score = 0

    def draw(self, surface):
        for p in self.positions:
            self.r = pygame.Rect((p[0], p[1]), (gridsize, gridsize))

            pygame.draw.rect(surface, self.color, self.r)
            pygame.draw.rect(surface, (93, 216, 228), self.r, 1)

    def check_exit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def string_visualization(self, surface, apple, body):
        "Scale the coordinates of the head and the body"
        self.start = [int(self.positions[0][0]/20), int(self.positions[0][1]/20)]
        self.end = [int(apple[0]/20), int(apple[0]/20)]
        self.body = []

        "Clean the body list. Then append all new locations of body parts"
        if len(self.body) != 1:
            del self.body[0:]
            for i in range(len(body)):
                if i + 1 < len(body):
                    self.body.append([int(body[i + 1][0]/20), int(body[i + 1][1]/20)])

                else:
                    pass

        else:
            self.body = self.start

        "Create simulations of the apple and the snake's head. This must be in a try statement cause at first, there is no index"
        try:
            maze[self.start[0]][self.start[1]] = "O" # Snake's head
            maze[self.end[0]][self.end[1]] = "X" # Apple, but the snake won't know

        except IndexError:
            pass   

        "Draw the snake's body"
        try:
            for i in self.body:
                maze[i[0]][i[1]] = "#" # Snake's body
        
        except:
            pass

        "Clean maze and replace everything"
        del maze[0:]
        #             1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21   22   23   24
        maze.append(["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
        maze.append(["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"])

    def ai(self, start, surface):
        self.up_x_1_index = []
        self.up_x_2_index = []
        self.left_x_1_index = []
        self.left_x_2_index = []
        self.right_x_1_index = []
        self.right_x_2_index = []
        self.safe_visible_moves = []        

        try:
            "Create the index of what the snake see's depending on which position he is in."
            if self.direction == up:
                "up"
                self.up_x_1_index = [self.start[0], self.start[1] - 1]
                self.up_x_2_index = [self.start[0], self.start[1] - 2]
                self.left_x_1_index = [self.start[0] + 1, self.start[1]]
                self.left_x_2_index = [self.start[0] + 1, self.start[1] - 1]      
                self.right_x_1_index = [self.start[0] - 1, self.start[1]]
                self.right_x_2_index = [self.start[0] - 1, self.start[1] - 1] 

            elif self.direction == down:
                "down"
                self.up_x_1_index = [self.start[0], self.start[1] + 1]
                self.up_x_2_index = [self.start[0], self.start[1] + 2]
                self.left_x_1_index = [self.start[0] - 1, self.start[1]]
                self.left_x_2_index = [self.start[0] - 1, self.start[1] + 1]
                self.right_x_1_index = [self.start[0] + 1, self.start[1]]
                self.right_x_2_index = [self.start[0] + 1, self.start[1] + 1]    

            elif self.direction == left:
                "left"        
                self.up_x_1_index = [self.start[0] - 1, self.start[1]]  
                self.up_x_2_index = [self.start[0] - 2, self.start[1]] 
                self.left_x_1_index = [self.start[0], self.start[1] - 1]  
                self.left_x_2_index = [self.start[0], self.start[1] - 1]
                self.right_x_1_index = [self.start[0] - 1, self.start[1] + 1]
                self.right_x_2_index = [self.start[0] - 1, self.start[1] + 1]

            else:
                "right"
                self.up_x_1_index = [self.start[0] + 1, self.start[1]]
                self.up_x_2_index = [self.start[0] + 2, self.start[1]]
                self.left_x_1_index = [self.start[0], self.start[1] + 1]
                self.left_x_2_index = [self.start[0] + 1, self.start[1] + 1]
                self.right_x_1_index = [self.start[0], self.start[1] - 1]
                self.right_x_2_index = [self.start[0] + 1, self.start[1] - 1] 

        except IndexError:
            pass  

        "Append safe moves that it can see"
        try:
            if maze[self.up_x_1_index[0]][self.up_x_1_index[1]] != "#":
                self.safe_visible_moves.append(self.direction)

            else:
                pass

            if maze[self.right_x_1_index[0]][self.right_x_1_index[1]] != "#":
                if self.direction == left:
                    self.safe_visible_moves.append(up)
                
                elif self.direction == right:
                    self.safe_visible_moves.append(down)

                elif self.direction == down:
                    self.safe_visible_moves.append(left)

                else:
                    self.safe_visible_moves.append(right)

            else:
                pass

            if maze[self.left_x_1_index[0]][self.left_x_1_index[1]] != "#":             
                if self.direction == left:
                    self.safe_visible_moves.append(down)
                
                elif self.direction == right:
                    self.safe_visible_moves.append(up)

                elif self.direction == down:
                    self.safe_visible_moves.append(right)

                else:
                    self.safe_visible_moves.append(left)
            else:
                pass

        except:
            pass

        #"Safe visible moves"
        #for safe_move in self.safe_visible_moves:
        #    square_drawer((safe_move * 24), surface)


        "What it can see"
        square_drawer(self.up_x_1_index, surface)
        square_drawer(self.up_x_2_index, surface)
        square_drawer(self.left_x_1_index, surface)
        square_drawer(self.left_x_2_index, surface)
        square_drawer(self.right_x_1_index, surface)
        square_drawer(self.right_x_2_index, surface) 

        try:
            "If it's going to crash, pick a random safe move"
            self.is_right_dangerous = maze[self.up_x_1_index[0]][self.up_x_1_index[1]] == "#" and self.direction == right
            self.is_left_dangerous = maze[self.left_x_1_index[0]][self.left_x_1_index[1]] == "#" and self.direction == left
            self.is_up_dangerous = maze[self.right_x_1_index[0]][self.right_x_1_index[1]] == "#" and self.direction == up
            
            if  self.is_right_dangerous or self.is_left_dangerous or self.is_up_dangerous:
                self.turn(random.choice(self.safe_visible_moves))    
        except:
            pass     

        del self.safe_visible_moves