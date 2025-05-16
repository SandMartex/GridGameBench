import random
import numpy as np

class Game2048:
    def __init__(self, n):
        self.n = n
        self.grid = np.zeros((n, n), dtype=np.int32)
        self.steps = 0
        self.score = 0
        pos = self.random_init()
        self.grid[pos[0]] = 2
        self.grid[pos[1]] = 4

        self.history = [self.grid]
        self.direction = []
        self.status = "actv" # 4 status: actv, over, void, dead
        self.last_op = ""

    def random_init(self):
        positions = [(i, j) for i in range(self.n) for j in range(self.n)]
        return random.sample(positions, 2)

    def merge(self, array):
        if np.all(array == 0):
            return array
        filtered = [x for x in array if x != 0]
        merged = []
        i = 0
        while i < len(filtered):
            if i < len(filtered) - 1 and filtered[i] == filtered[i + 1]:
                merged.append(filtered[i] * 2)
                self.score += filtered[i] * 2
                i += 2
            else:
                merged.append(filtered[i])
                i += 1
        merged += [0] * (self.n - len(merged))
        return np.array(merged)

    def up(self):
        new_grid = np.zeros_like(self.grid)
        for i in range(self.n):
            new_grid[:, i] = self.merge(self.grid[:, i])
        return new_grid

    def down(self):
        new_grid = np.zeros_like(self.grid)
        for i in range(self.n):
            new_grid[:, i] = self.merge(self.grid[:, i][::-1])[::-1]
        return new_grid

    def left(self):
        new_grid = np.zeros_like(self.grid)
        for i in range(self.n):
            new_grid[i] = self.merge(self.grid[i])
        return new_grid

    def right(self):
        new_grid = np.zeros_like(self.grid)
        for i in range(self.n):
            new_grid[i] = self.merge(self.grid[i][::-1])[::-1]
        return new_grid

    def end_game(self):
        if 0 in self.grid:
            return False
        for i in range(self.n):
            for j in range(self.n - 1):
                if self.grid[i][j] == self.grid[i][j + 1]:
                    return False
                if self.grid[j][i] == self.grid[j + 1][i]:
                    return False
        return True

    def move(self, direction: str):
        direction = direction.lower()
        if direction == "up":
            new_grid = self.up()
        elif direction == "down":
            new_grid = self.down()
        elif direction == "left":
            new_grid = self.left()
        elif direction == "right":
            new_grid = self.right()
        else:
            return "dead"
        if np.array_equal(new_grid, self.grid):
            self.last_op = direction
            return "void"
        self.grid = new_grid
        indices = np.where(self.grid == 0)
        random_index = np.random.choice(indices[0].size)
        selected_row = indices[0][random_index]
        selected_col = indices[1][random_index]
        if random.random() > .5:
            self.grid[selected_row, selected_col] = 2
        else:
            self.grid[selected_row, selected_col] = 4
        if indices[0].size == 1:
            if self.end_game():
                return "over"
        return "actv"

    def step(self, direction: str):
        self.status = self.move(direction)
        if self.status == "actv" or self.status == "over":
            self.steps += 1
            self.history.append(self.grid)
            self.direction.append(direction)
        return self.to_text(), str(self.score), self.status

    def to_text(self):
        return "\n".join([" ".join(map(str, row)) for row in self.grid])

    def get_status(self):
        status = f"The current score is {self.score}\n"
        invalids = []
        score = self.score
        if np.array_equal(self.up(), self.grid):
            invalids.append("UP")
        if np.array_equal(self.down(), self.grid):
            invalids.append("DOWN")
        if np.array_equal(self.left(), self.grid):
            invalids.append("LEFT")
        if np.array_equal(self.right(), self.grid):
            invalids.append("RIGHT")
        self.score = score
        status += self.to_text()
        if self.status == "void":
            status += f"\nYour last move is {self.last_op}, which is an invalid direction. YOU CAN NOT USE {' '.join(invalids)}"
        return status
