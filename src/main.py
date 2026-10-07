import pygame
import sys

from constants import WINDOW_WIDTH, WINDOW_HEIGHT
from gamegrid import GameGrid
from sprites import Block

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    game_grid = GameGrid()

    peices, border, updatable, drawable = [pygame.sprite.Group() for _ in range(4)]

    GameGrid.containers = (updatable,)

    ## Initializing game grid

    ## Draw left border using blocks
    for y in range(2,22):
        border_block = Block(-1, y, (100, 100, 100))
        border.add(border_block)
        drawable.add(border_block)

    ## Draw right border using blocks
    for y in range(2,22):
        border_block = Block(10, y, (100, 100, 100))
        border.add(border_block)
        drawable.add(border_block)

    ## Draw bottom border using blocks
    for x in range (-1, 11):
        border_block = Block(x, 22, (100, 100, 100))
        border.add(border_block)
        drawable.add(border_block)
    


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        drawable.draw(screen)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()