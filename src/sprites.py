import pygame
from constants import BLOCK_SIZE, START_X, START_Y


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        self.update_pixel_position()

    def update_pixel_position(self):
        pixel_x = START_X + (self.x * BLOCK_SIZE)
        pixel_y = START_Y + ((self.y - 2) * BLOCK_SIZE)
        self.rect.topleft = (pixel_x, pixel_y)

    def update(self):
        self.update_pixel_position()