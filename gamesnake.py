import random
import numpy as np

class GameSnake:
    def __init__(self, n):
        self.n = n
        self.grid = np.zeros((n, n), dtype=np.int32)
        self.steps = 0
        self.score = 0
        pos = self.random_init()
        self.grid[pos[0]] = 1
        self.grid[pos[1]] = -1
        self.snake = [pos[0]]
        self.food = pos[1]

        self.history = [self.grid]
        self.direction = []
        self.status = "actv" # 4 status: actv, over, void, dead
        self.last_op = ""

    def random_init(self):
        positions = [(i, j) for i in range(self.n) for j in range(self.n)]
        return random.sample(positions, 2)

    def generate_food(self):
        empty_cells = [(i, j) for i in range(self.n) for j in range(self.n) if (i, j) not in self.snake]
        if not empty_cells:
            self.status = "over"
            return False
        self.food = random.choice(empty_cells)
        self.grid[self.food] = -1
        return True

    def move(self, direction):
        directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
        if direction not in directions:
            return "dead"
        oppo = {"up": "down", "down": "up", "left": "right", "right": "left"}
        if self.last_op == oppo[direction]:
            return "void"
        head = self.snake[-1]
        dx, dy = directions[direction]
        new_head = (head[0] + dx, head[1] + dy)
        if not (0 <= new_head[0] < self.n and 0 <= new_head[1] < self.n) or new_head in self.snake:
            return "over"

        self.snake.append(new_head)
        self.steps += 1
        if new_head == self.food:
            self.score += 1
            self.generate_food()
        else:
            tail = self.snake.pop(0)
            self.grid[tail] = 0
        self.grid = np.zeros((self.n, self.n), dtype=np.int32)
        for i in range(len(self.snake)):
            self.grid[self.snake[-i-1]] = i+1
        self.grid[self.food] = -1
        return 'actv'

    def step(self, direction, number):
        for _ in range(number):
            self.status = self.move(direction)
            if self.status != 'actv':
                break
        if self.status == "actv" or self.status == "over":
            self.steps += 1
            self.history.append(self.grid)
            self.direction.append(direction)
            self.last_op = direction
        return self.to_text(), str(self.score), self.status

    def to_text(self):
        return "\n".join([" ".join(map(str, row)) for row in self.grid])

    def get_status(self):
        status = f"Score: {self.score}, Steps: {self.steps}, Status: {self.status}\n"
        status += self.to_text()
        oppo = {"up": "down", "down": "up", "left": "right", "right": "left"}
        if self.status == "void":
            status += f"\nYour last valid move is {self.last_op}, and your last move is {oppo[self.last_op]}, which is an invalid direction. YOU CAN NOT USE {oppo[self.last_op]}"
        return status
