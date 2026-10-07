import pygame
import sys

from tetris.constants import WINDOW_WIDTH, WINDOW_HEIGHT
from tetris.gamegrid import GameGrid
from tetris.sprites import Block

def main():
    pygame.init()
    pygame.key.set_repeat(170, 50)
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    peices, border, updatable, drawable = [pygame.sprite.Group() for _ in range(4)]

    GameGrid.containers = (updatable,)
    Block.containers = (drawable, updatable)

    ## Draw left border using blocks
    for y in range(2, 22):
        border.add(Block(-1, y, (100, 100, 100)))

    ## Draw right border using blocks
    for y in range(2, 22):
        border.add(Block(10, y, (100, 100, 100)))

    ## Draw bottom border using blocks
    for x in range(-1, 11):
        border.add(Block(x, 22, (100, 100, 100)))

    game_grid = GameGrid()
    space_held = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game_grid.rotate_piece()
                elif event.key == pygame.K_LEFT:
                    game_grid.move_piece(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    game_grid.move_piece(1, 0)
                elif event.key == pygame.K_DOWN:
                    game_grid.move_piece(0, 1)
                elif event.key == pygame.K_SPACE and not space_held:
                    space_held = True
                    game_grid.hard_drop()
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                space_held = False

        updatable.update()

        screen.fill((0, 0, 0))
        drawable.draw(screen)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()