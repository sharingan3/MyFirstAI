import pygame
import random
from grid import all_free_space, gridsize

class Food:
    def __init__(self):
        self.position = (100, 100)
        self.color = (255, 0, 0)

        self.randomize_position()

    def randomize_position(self):
        self.position = random.choice(all_free_space)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)