import pygame


class Checkerboard:
    def __init__(self, block_size, screen_width, screen_height):
        self.block_size = block_size
        self.screen_width = screen_width
        self.screen_height = screen_height

    def draw(self, screen):
        i = 0
        for x in range(0, self.screen_width, self.block_size):
            for y in range(0, self.screen_height, self.block_size):
                if i % 2 == 0:
                    pygame.draw.rect(screen, (162, 209, 72), (x, y, self.block_size, self.block_size))
                else:
                    pygame.draw.rect(screen, (170, 215, 80), (x, y, self.block_size, self.block_size))
                i += 1
            i += 1



