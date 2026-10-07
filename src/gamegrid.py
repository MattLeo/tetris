import pygame

class GameGrid():
    def __init__(self):
        self.width = 10
        self.height = 22
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]