import random
import sys
import pygame

from tetris.constants import DROP_INTERVAL
from tetris.tetromino import Tetromino, SHAPES


class GameGrid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(self.containers)
        self.width = 10
        self.height = 22
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.last_drop = pygame.time.get_ticks()
        self.spawn_piece()

    def is_valid(self, cells):
        for x, y in cells:
            if x < 0 or x >= self.width or y >= self.height:
                return False
            if self.grid[y][x] != 0:
                return False
        return True

    def rotate_piece(self):
        new_rotation = (self.current.rotation + 1) % 4
        candidate = self.current.cells(rotation=new_rotation)
        if self.is_valid(candidate):
            self.current.rotate()

    def move_piece(self, dx, dy):
        candidate = self.current.cells(x=self.current.x + dx, y=self.current.y + dy)
        if self.is_valid(candidate):
            self.current.move(dx, dy)
            return True
        return False

    def hard_drop(self):
        while self.move_piece(0, 1):
            pass
        self.settle()

    def lock_piece(self):
        for block in self.current.blocks:
            self.grid[block.y][block.x] = block

    def clear_lines(self):
        remaining = [row for row in self.grid if any(cell == 0 for cell in row)]
        cleared = self.height - len(remaining)
        for row in self.grid:
            if all(cell != 0 for cell in row):
                for block in row:
                    block.kill()
        self.grid = [[0 for _ in range(self.width)] for _ in range(cleared)] + remaining
        for y, row in enumerate(self.grid):
            for block in row:
                if block != 0:
                    block.y = y

    def spawn_piece(self):
        self.current = Tetromino(random.choice(list(SHAPES)))
        if not self.is_valid(self.current.cells()):
            print("Game over")
            pygame.quit()
            sys.exit()

    def settle(self):
        self.lock_piece()
        self.clear_lines()
        self.spawn_piece()
        self.last_drop = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_drop >= DROP_INTERVAL:
            self.last_drop = now
            if not self.move_piece(0, 1):
                self.settle()