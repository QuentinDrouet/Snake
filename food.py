import pygame
import math
import random
from snake import Snake


class Food:
    def __init__(self, x, y, block_size, malus):
        self.x = x
        self.y = y
        self.block_size = block_size
        self.malus = malus
        self.score = 0
        self.controls_reverse = False
        self.has_eaten = False

    def draw(self, screen):
        if not self.malus:
            pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.block_size, self.block_size))
        elif self.malus:
            pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.block_size, self.block_size))

    def collision(self, screen, snake, snake_x, snake_y):
        screen_size = screen.get_rect()
        dist = math.hypot(snake_x - self.x, snake_y - self.y)
        if dist < self.block_size:
            if not self.malus:
                self.has_eaten = True
                self.score += 1
                snake.length += 1
            else:
                self.score += 1
                if self.controls_reverse:
                    self.controls_reverse = False
                    snake.body.reverse()
                else:
                    self.controls_reverse = True
                    snake.body.reverse()
            self.x = int(random.randint(0, screen_size[2]) / self.block_size) * self.block_size
            self.y = int(random.randint(0, screen_size[3]) / self.block_size) * self.block_size

