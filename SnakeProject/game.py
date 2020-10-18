import pygame
from apple import Food
from snake import Snake
from grid import drawGrid, WallCell, screen_width, screen_height, all_obstacle_pos, all_free_space

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
    food = Food()

    "Define the scores font"
    myfont = pygame.font.SysFont("monospace", 16)

    "Begin the game loop. To stop game loop, set running t False"
    running = True

    while running:
        clock.tick(10)
        snake.check_exit()
        drawGrid(surface)
        snake.move()
        snake.string_visualization(surface, food.position, snake.positions)
        snake.ai(snake.positions[0], surface)

        "Empty list then add snake body positions"
        del all_obstacle_pos[0][:]
        for i in snake.positions:
            if i != snake.positions[0]:
                all_obstacle_pos[0].append(i)

            else:
                pass

        "Use loop to draw the walls"
        for i in range(0, 481, 20):
            wall_cell.create_cell(surface, "up", i)
            wall_cell.create_cell(surface, "left", i)
            wall_cell.create_cell(surface, "down", i)
            wall_cell.create_cell(surface, "right", i)

        "Check if any obstacles is found in all_free_space. This is done after building the list and drawing the snake so we know that all obstacles have already been drawn"
        for obstacle in range(len(all_obstacle_pos)):
            for i in all_obstacle_pos[obstacle]:
                if i in all_free_space:
                    all_free_space.remove(i)

        "Detect if the snake's head is in the same location as the apple"
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position()

        else:
            pass

        "Redraw everything to update the screen"
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0,0))

        "Make the game over text"
        game_over_font = pygame.font.SysFont('Bowlby One SC', 24)
        textsurface = game_over_font.render('GAME OVER', False, (0, 0, 0))

        "Check if crashed"
        for snake_pos in all_obstacle_pos[0]:
            if snake.positions[0] == snake_pos:
                screen.blit(textsurface, (175, 200))
                snake.reset()

            else:
                pass

        for wall_pos in all_obstacle_pos[1]:
            if snake.positions[0] == wall_pos:
                screen.blit(textsurface, (175, 200))
                snake.reset()

            else:
                pass

        "Re-put everything back"
        for i in range(0, 480, 20):
            for j in range(0, 480, 20):
                if (i, j) not in all_free_space:
                    all_free_space.append((i, j))

                else:
                    pass

        "Draw the score on the top left corner"
        text = myfont.render("Score {0}".format(snake.score), 1, (0, 0, 0))
        screen.blit(text, (5, 3))
        pygame.display.update()