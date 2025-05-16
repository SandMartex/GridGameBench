import random
import numpy as np

class GameTetris:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = np.zeros((rows, cols), dtype=np.int32)
        self.score = 0
        self.steps = 0
        self.status = "actv"  # Game status: actv (active), over (game over)
        self.current_tetromino = None
        self.tetromino_pos = None
        self.spawn_tetromino()

        self.history = [self.grid.copy()]
        self.last_op = ""

    def spawn_tetromino(self):
        tetrominoes = {
            "I": np.array([[1, 1, 1, 1]]),  # Line
            "O": np.array([[1, 1], [1, 1]]),  # Square
            # "T": np.array([[0, 1, 0], [1, 1, 1]]),  # T-shape
            # "L": np.array([[1, 0], [1, 0], [1, 1]]),  # L-shape
            # "J": np.array([[0, 1], [0, 1], [1, 1]]),  # Reverse L-shape
            # "S": np.array([[0, 1, 1], [1, 1, 0]]),  # S-shape
            # "Z": np.array([[1, 1, 0], [0, 1, 1]])   # Reverse S-shape
        }

        shape_key = random.choice(list(tetrominoes.keys()))
        self.current_tetromino = tetrominoes[shape_key]
        self.tetromino_pos = (0, (self.cols - self.current_tetromino.shape[1]) // 2)

        self.status = self.is_valid_position(self.tetromino_pos)

    def is_valid_position(self, pos):
        tetromino = self.current_tetromino
        for i in range(tetromino.shape[0]):
            for j in range(tetromino.shape[1]):
                if tetromino[i, j] == 1:
                    x, y = pos[0] + i, pos[1] + j
                    if x < 0 or x >= self.rows or y < 0 or y >= self.cols:
                        return "void"
                    elif self.grid[x, y] != 0:
                        return "over"
        return "actv"

    def place_tetromino(self):
        tetromino = self.current_tetromino
        for i in range(tetromino.shape[0]):
            for j in range(tetromino.shape[1]):
                if tetromino[i, j] == 1:
                    x, y = self.tetromino_pos[0] + i, self.tetromino_pos[1] + j
                    self.grid[x, y] = 1

    def clear_lines(self):
        lines_to_clear = [i for i in range(self.rows) if all(self.grid[i])]
        rows_cleared = len(lines_to_clear)

        if rows_cleared > 0:
            for row in lines_to_clear:
                self.grid[1 : row + 1] = self.grid[:row]
                self.grid[0] = 0
            self.score += rows_cleared

        return rows_cleared

    def operate(self, left_distance, rotations):
        rotated = np.rot90(self.current_tetromino, -rotations)
        old_tetromino = self.current_tetromino
        self.current_tetromino = rotated
        new_pos = (self.tetromino_pos[0], left_distance)
        self.status = self.is_valid_position(new_pos)
        if self.status == 'actv':
            self.tetromino_pos = new_pos
        else:
            self.current_tetromino = old_tetromino

    def step(self, left_distance, rotations):
        self.last_op = {0: 'Static', 1: 'Rotate'}[rotations] + f' {left_distance}'

        self.operate(left_distance, rotations)

        if self.status == 'actv':
            while self.is_valid_position((self.tetromino_pos[0] + 1, self.tetromino_pos[1])) == 'actv':
                self.tetromino_pos = (self.tetromino_pos[0] + 1, self.tetromino_pos[1])

            self.place_tetromino()
            self.clear_lines()
            self.spawn_tetromino()

            self.steps += 1
            self.history.append(self.grid.copy())

        return self.to_text(), str(self.score), self.status

    def to_text(self):
        grid_copy = self.grid.copy()
        tetromino = self.current_tetromino
        for i in range(tetromino.shape[0]):
            for j in range(tetromino.shape[1]):
                if tetromino[i, j] == 1:
                    x, y = self.tetromino_pos[0] + i, self.tetromino_pos[1] + j
                    if 0 <= x < self.rows and 0 <= y < self.cols:
                        grid_copy[x, y] = 2
        return "\n".join([" ".join(map(str, row)) for row in grid_copy])

    def get_status(self):
        status = f"Score: {self.score}, Steps: {self.steps}, Status: {self.status}\n"
        status += self.to_text()
        if self.status == "void":
            status += f"\nYour last move is {self.last_op}, which is an invalid direction. YOU CAN NOT USE {self.last_op}"
        return status
