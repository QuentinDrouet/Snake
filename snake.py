import pygame
from math import *


class Snake:
    def __init__(self, block_size):
        self.length = 1
        self.body = []
        self.block_size = block_size
        self.snake_coords = [block_size, block_size]
        self.x, self.y = (1, 0)
        self.collision = False
        self.quit = False

    def move(self, screen, x, y):
        # add new snake coordinates to the entire snake
        self.body.append([x, y])
        # check if the length of the current snake is > than the previous length
        if len(self.body) > self.length:
            del self.body[0]
        if self.body[-1] in self.body[0:-1]:
            self.collision = True

        # get the width and height of the window dor the collision below (instead of adding screen width and height
        # in argument)
        screen_size = screen.get_rect()

        for part in self.body:
            pygame.draw.rect(screen, (90, 122, 250), (part[0], part[1], self.block_size, self.block_size))

        # check collision with walls
        if self.body[-1][0] == screen_size[2] or self.body[-1][0] == - self.block_size or self.body[-1][1] == \
                screen_size[3] or self.body[-1][
            1] == - self.block_size:
            self.collision = True

    def controls(self, controls_reverse):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            if event.type == pygame.KEYDOWN:
                # change direction (check last direction)
                if event.key == pygame.K_RIGHT and (self.x, self.y) != (-1, 0):
                    (self.x, self.y) = (1, 0)
                if event.key == pygame.K_LEFT and (self.x, self.y) != (1, 0):
                    (self.x, self.y) = (-1, 0)
                if event.key == pygame.K_UP and (self.x, self.y) != (0, -1):
                    (self.x, self.y) = (0, 1)
                if event.key == pygame.K_DOWN and (self.x, self.y) != (0, 1):
                    (self.x, self.y) = (0, -1)

        # update snake coordinates with direction
        if (self.x, self.y) == (0, 1):
            if not controls_reverse:
                self.snake_coords[1] -= self.block_size
            else:
                self.snake_coords[1] += self.block_size
        if (self.x, self.y) == (0, -1):
            if not controls_reverse:
                self.snake_coords[1] += self.block_size
            else:
                self.snake_coords[1] -= self.block_size
        if (self.x, self.y) == (-1, 0):
            if not controls_reverse:
                self.snake_coords[0] -= self.block_size
            else:
                self.snake_coords[0] += self.block_size
        if (self.x, self.y) == (1, 0):
            if not controls_reverse:
                self.snake_coords[0] += self.block_size
            else:
                self.snake_coords[0] -= self.block_size
