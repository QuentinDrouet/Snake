import pygame
import math
import random
from checkerboard import Checkerboard
from snake import Snake
from food import Food

module_charge = pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 80)

# Variables
screen_width = 800
screen_height = 800
block_size = 50
loop = True
controls_reverse = False

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")

# Objects
board = Checkerboard(block_size, screen_width, screen_height)
snake = Snake(block_size)
food = Food(int(random.randint(0, screen_width) / block_size) * block_size,
            int(random.randint(0, screen_height) / block_size) * block_size,
            block_size, False)
malus = Food(int(random.randint(0, screen_width) / block_size) * block_size,
             int(random.randint(0, screen_height) / block_size) * block_size,
             block_size, True)
clock = pygame.time.Clock()
board.draw(screen)

while loop:

    # change position according to direction
    snake.controls(controls_reverse)

    # if the window is closed
    if snake.quit:
        loop = False

    # draw the checkerboard
    board.draw(screen)

    # generate food
    food.draw(screen)

    # change malus coordinates when eating food
    if food.has_eaten:
        malus.x = int(random.randint(0, screen_width) / malus.block_size) * malus.block_size
        malus.y = int(random.randint(0, screen_height) / malus.block_size) * malus.block_size
        food.has_eaten = False

    malus.draw(screen)

    # check collisions between the snake and food/malus
    malus.collision(screen, snake, snake.snake_coords[0], snake.snake_coords[1])
    food.collision(screen, snake, snake.snake_coords[0], snake.snake_coords[1])

    # handle change of controls in the Food class
    if malus.controls_reverse:
        controls_reverse = True
    elif not malus.controls_reverse:
        controls_reverse = False

    snake.move(screen, snake.snake_coords[0], snake.snake_coords[1])

    # if the snake collides with itself or walls
    if snake.collision:
        loop = False

    # display score
    text_surface = my_font.render(str(food.score) or str(malus.score), False, (0, 0, 0))
    screen.blit(text_surface, (screen_width / 2, 0))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
