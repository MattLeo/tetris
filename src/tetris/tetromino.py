from tetris.sprites import Block

SHAPES = {
    "T": [
        [(1, 0), (0, 1), (1, 1), (2, 1)], # initial rotation
        [(1, 0), (1, 1), (2, 1), (1, 2)], # 90 degrees rotation
        [(0, 1), (1, 1), (2, 1), (1, 2)], # 180 degrees rotation
        [(1, 0), (0, 1), (1, 1), (1, 2)]  # 270 degrees rotation
    ],
    "I": [
        [(0, 1), (1, 1), (2, 1), (3, 1)], # initial rotation
        [(2, 0), (2, 1), (2, 2), (2, 3)], # 90 degrees rotation
        [(0, 2), (1, 2), (2, 2), (3, 2)], # 180 degrees rotation
        [(1, 0), (1, 1), (1, 2), (1, 3)]  # 270 degrees rotation
    ],
    "O": [
        [(1, 0), (2, 0), (1, 1), (2, 1)], # initial rotation
        [(1, 0), (2, 0), (1, 1), (2, 1)], # 90 degrees rotation
        [(1, 0), (2, 0), (1, 1), (2, 1)], # 180 degrees rotation
        [(1, 0), (2, 0), (1, 1), (2, 1)]  # 270 degrees rotation
    ],
    "L": [
        [(2, 0), (0, 1), (1, 1), (2, 1)], # initial rotation
        [(1, 0), (1, 1), (1, 2), (2, 2)], # 90 degrees rotation
        [(0, 1), (1, 1), (2, 1), (0, 2)], # 180 degrees rotation
        [(0, 0), (1, 0), (1, 1), (1, 2)]  # 270 degrees rotation
    ],
    "J": [
        [(0, 0), (0, 1), (1, 1), (2, 1)], # initial rotation
        [(1, 0), (2, 0), (1, 1), (1, 2)], # 90 degrees rotation
        [(0, 1), (1, 1), (2, 1), (2, 2)], # 180 degrees rotation
        [(1, 0), (1, 1), (1, 2), (0, 2)]  # 270 degrees rotation
    ],
    "S": [
        [(1, 0), (2, 0), (0, 1), (1, 1)], # initial rotation
        [(1, 0), (1, 1), (2, 1), (2, 2)], # 90 degrees rotation
        [(1, 1), (2, 1), (0, 2), (1, 2)], # 180 degrees rotation
        [(0, 0), (0, 1), (1, 1), (1, 2)]  # 270 degrees rotation
    ],
    "Z": [
        [(0, 0), (1, 0), (1, 1), (2, 1)], # initial rotation
        [(2, 0), (1, 1), (2, 1), (1, 2)], # 90 degrees rotation
        [(0, 1), (1, 1), (1, 2), (2, 2)], # 180 degrees rotation
        [(1, 0), (0, 1), (1, 1), (0, 2)]  # 270 degrees rotation
    ],
}
COLORS = {
    "I": (0, 240, 240),    # cyan
    "O": (240, 240, 0),    # yellow
    "T": (160, 0, 240),    # purple
    "S": (0, 240, 0),      # green
    "Z": (240, 0, 0),      # red
    "J": (0, 0, 240),      # blue
    "L": (240, 160, 0),    # orange
}

class Tetromino:
    def __init__(self, shape):
        self.shape = shape
        self.rotation = 0
        self.x = 3
        self.y = 0
        self.blocks = [Block(self.x + dx, self.y + dy, COLORS[shape]) for dx, dy in SHAPES[shape][self.rotation]]

    def cells(self, x=None, y=None, rotation=None):
        if x is None:
            x = self.x
        if y is None:
            y = self.y
        if rotation is None:
            rotation = self.rotation
        return [(x + dx, y + dy) for dx, dy in SHAPES[self.shape][rotation]]

    def _sync_blocks(self):
        for block, (x, y) in zip(self.blocks, self.cells()):
            block.x, block.y = x, y

    def rotate(self):
        self.rotation = (self.rotation + 1) % 4
        self._sync_blocks()

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self._sync_blocks()