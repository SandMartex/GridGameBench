RULES_2048 = """
Rules and Objective of the Game 2048
The objective of 2048 is to slide and combine tiles on a 4x4 grid to create a tile with the number 2048 or higher. The game begins with two tiles, either "2" or "4", on the grid, and after each move, a new "2" or "4" tile appears randomly on an empty space. You can slide tiles in four directions (up, down, left, or right), and all tiles move as far as possible in the chosen direction until they encounter another tile or the edge of the grid; each move must result in at least one tile moving. If two tiles with the same number collide, they merge into one tile with a value equal to their sum, and each merge adds the value of the resulting tile to your score. The game ends when there are no valid moves left, meaning no empty spaces and no possible merges, and you win by creating a tile with the number 2048, though you can continue playing to achieve higher numbers. The game combines strategy and luck, as players aim to maximize merges and keep the largest tile in a corner while avoiding moves that disrupt the grid.
"""

COT_2048 = """
Status:
0 8 16 64
2 4 2 8
2 8 2 4
0 0 2 0
Thought: The current largest number is 64, and we need to keep it in the corner. Therefore, the possible directions are up or right. At the same time, choosing up will result in multiple merges, so we prefer to choose up.
Operation: Up
Status after operation:
4 8 16 64
0 4 4 8
0 8 2 4
0 0 0 0

Status:
4 8 16 64
0 4 4 8
0 8 2 4
0 4 0 0
Thought: The current largest number is 64, and we need to keep it in the corner. Therefore, the possible directions are up, left, or right. At the same time, choosing right will result in multiple merges, so we prefer to choose right.
Operation: Right
Status after operation:
4 8 16 64
0 0 8 8
0 8 2 4
0 0 0 0

Status:
4 8 16 64
0 0 8 8
0 8 2 4
0 0 2 0
Thought: The current largest number is 64, and we need to keep it in the corner. Therefore, the possible directions are up, left, or right. At the same time, choosing up will result in multiple merges, so we prefer to choose up.
Operation: Up
Status after operation:
4 16 16 64
0 0 8 8
0 0 2 4
0 0 2 0

Status:
4 16 16 64
0 4 8 8
0 0 2 4
0 0 2 0
Thought: The current largest number is 64, and we need to keep it in the corner. Therefore, the possible directions are up or right. At the same time, choosing right will result in multiple merges, so we prefer to choose right.
Operation: Right
Status after operation:
0 4 32 64
0 0 4 16
0 0 2 4
0 0 0 2

Status:
0 4 32 64
0 0 4 16
2 0 2 4
0 0 0 2
Thought: The current largest number is 64, and we need to keep it in the corner. Therefore, the possible directions are up or right. At the same time, choosing up will fill the first row, enabling the option to choose up, left, or right in future rounds. Therefore, we choose up.
Operation: Up
Status after operation:
2 4 32 64
0 0 4 16
0 0 2 4
0 0 0 2

Status:
2 8 0 2
16 0 0 0
64 4 2 0
64 16 0 0
Thought: We notice that choosing down allows the current largest number, 64, to merge. At the same time, the newly generated largest number, 128, can also remain in the corner. Therefore, we prefer to choose down.
Operation: Down
Status after operation:
0 0 0 0
2 8 0 0
16 4 0 0
128 16 2 2
"""

RULES_SNAKE = """
Rules and Objective of the Game Snake
The game is played on a grid where each cell is represented by an integer. The value 0 represents an empty cell, -1 represents food, and positive integers (1 and higher) represent the snake's body. The snake's head is denoted by 1, and the largest number represents the snake's tail, indicating the order of its body segments. The snake moves based on operations provided by the player or AI, where each operation specifies a direction (up, down, left, or right) and a number of steps to move. The snake moves continuously in the specified direction for the given number of steps. A move is valid if the snake does not collide with itself or the grid boundaries during the specified movement. When the snake's head enters a cell containing -1 (food), the food is eaten, and the snake's length increases by one. The tail does not move for that step, and the food is removed from the grid. If the snake moves into a cell containing its own body or outside the grid boundary, the game ends. The goal of the game is to eat as much food as possible, with the score being the total number of food items eaten by the snake. The game ends when the snake collides with itself or the wall, or if there are no valid moves left.
"""

COT_SNAKE = """
Status:
1 0 0 0 0 0 0 0
0 0 0 0 0 0 -1 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
Thought: Currently, the length of the snake is 1, and there is no need to consider the body. But the up and left direction is blocked by the wall, so it can only move right or down. We find that the food is currently located to the bottom right of the snake, so our move is: down 1.
Operation: Down 1
Status after operation:
0 0 0 0 0 0 0 0
1 0 0 0 0 0 -1 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

Status:
0 0 0 0 0 0 0 0
1 0 0 0 0 0 -1 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
Thought: Currently, the length of the snake is 1, and the left direction is blocked by the wall, so it can move up, down or right. We can see that the food is currently located to the right of the snake, so our move is: right 6.
Operation: Right 6
Status after operation:
0 0 0 0 0 0 0 0
0 0 0 0 0 2 1 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

Status:
0 0 0 0 0 0 0 0
0 0 0 0 0 2 1 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 -1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
Thought: Currently, the length of the snake is 2, and need to consider the body, so it can only move to up, right or down. We can see that the food is currently located to the bottom right of the snake, so our move is: down 4.
Operation: Down 4
Status after operation:
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 2 0
0 0 0 0 0 0 1 -1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

Status:
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 2 0
0 0 0 0 0 0 1 -1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
Thought: Currently, the length of the snake is 2, and need to consider the body, so it can only move to left, right or down. We can see that the food is currently located to the right of the snake, so our move is: right 1.
Operation: Right 1
Status after operation:
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 3 0
0 0 0 0 0 0 2 1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

Status:
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 3 0
0 -1 0 0 0 0 2 1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
Thought: The current length of the snake is 3. The left direction is blocked by the body, and the right direction is blocked by the wall, so it can only move up or down. We can see that the food is currently on the right side of the snake, but we cannot move left. Therefore, our move is: up 1.
Operation: Up 1
Status after operation:
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1
0 -1 0 0 0 0 3 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

Status:
0 0 0 8 9 10 0 0
0 1 0 7 0 0 -1 0
0 2 0 6 0 0 0 0
0 3 4 5 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
Thought: Currently, the length of the snake is 10, and need to consider the body, so it can only move to up or left. We can see that the food is currently located to the right of the snake, but we can not go right. After going up, the snake can only go left. After going left, the snake can go up or down. In order to gain more choice, so our move is: left 1.
Operation: Left 1
Status after operation:
0 0 0 9 10 0 0 0
1 2 0 8 0 0 -1 0
0 3 0 7 0 0 0 0
0 4 5 6 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

Status:
0 0 0 9 10 0 0 0
1 2 0 8 0 0 -1 0
0 3 0 7 0 0 0 0
0 4 5 6 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
Thought: Currently, the length of the snake is 10. The right direction is blocked by the body, and the left direction is blocked by the wall, so it can only move to up or down. We can see that the food is currently located to the right of the snake, but we can not go right. After going up, the snake has no way to go. After going down, the snake can go right or down. In order to eat the food, so our move is: down 4.
Operation: Down 4
Status after operation:
0 0 0 0 0 0 0 0
4 5 0 0 0 0 -1 0
3 6 0 10 0 0 0 0
2 7 8 9 0 0 0 0
1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

Status:
0 0 0 0 0 0 0 0
4 5 0 0 0 0 -1 0
3 6 0 10 0 0 0 0
2 7 8 9 0 0 0 0
1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
Thought: The snake's current length is 10. The upper direction is blocked by the body, and the left direction is blocked by a wall, so it can move down or right. We can see that the food is currently located to the top right of the snake, so our move is: right 6.
Operation: Right 6
Status after operation:
0 0 0 0 0 0 0 0
10 0 0 0 0 0 -1 0
9 0 0 0 0 0 0 0
8 0 0 0 0 0 0 0
7 6 5 4 3 2 1 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

Status:
0 0 0 0 0 0 0 0
10 0 0 0 0 0 -1 0
9 0 0 0 0 0 0 0
8 0 0 0 0 0 0 0
7 6 5 4 3 2 1 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
Thought: The snake's current length is 10. The left direction is blocked by the body. We can see that the food is currently located to the top of the snake and the distance is 3, so our move is: up 3.
Operation: Up 3
Status after operation:
0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0
0 0 0 0 0 0 2 0
11 0 0 0 0 0 3 0
10 9 8 7 6 5 4 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

Status:
0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0
0 0 0 0 0 0 2 0
11 0 0 0 0 0 3 0
10 9 8 7 6 5 4 0
0 0 0 0 0 0 0 0
0 0 -1 0 0 0 0 0
0 0 0 0 0 0 0 0
Thought: The snake's current length is 11. The left, up and down direction is blocked by the body. The future plan is go right, go down then go left. We choose to move right first, so our move is: right 1.
Operation: Right 1
Status after operation:
0 0 0 0 0 0 0 0
0 0 0 0 0 0 2 1
0 0 0 0 0 0 3 0
0 0 0 0 0 0 4 0
11 10 9 8 7 6 5 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
"""

RULES_TETRIS = '''
Rules and Objective of the Game Tetris
The objective of Tetris is to control falling tetrominoes (shapes made of 4 blocks) to complete full horizontal rows on a grid, which are then cleared to earn points. The game begins with an empty grid, and tetrominoes spawn at the top, falling one step at a time. Players can rotate and move tetrominoes horizontally to position them, and once a tetromino can no longer move down, it locks into place, and a new tetromino appears. Rows are cleared when completely filled, and multiple rows cleared simultaneously yield higher points. The game ends when a new tetromino cannot spawn due to lack of space. The goal is to achieve the highest possible score by strategically placing tetrominoes to maximize cleared rows while avoiding the grid filling up.
'''

COT_TETRIS = """
Status:
0 0 2 2 0 0
0 0 2 2 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
Thought: We want to place it in the bottom left corner, so we need its distance from the left to be 0. We also do not need to rotate it, rotation is Static, and our operation is Static 0.
Operation: Static 0
Status after operation:
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
1 1 0 0 0 0
1 1 0 0 0 0

Status:
0 2 2 2 2 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
1 1 0 0 0 0
1 1 0 0 0 0
Thought: We want to place it in the bottom right corner, so we need its distance from the left to be 2. We also do not need to rotate it, rotation is Static, and our operation is Static 2.
Operation: Static 2
Status after operation:
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
1 1 0 0 0 0
1 1 1 1 1 1
Status after scoring:
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
1 1 0 0 0 0

Status:
0 0 2 2 0 0
0 0 2 2 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
1 1 0 0 0 0
Thought: We want to place it in the middle, so we need its distance from the left to be 2. We also do not need to rotate it, rotation is Static, and our operation is Static 2.
Operation: Static 2
Status after operation:
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 1 0 0
1 1 1 1 0 0

Status:
0 0 2 2 0 0
0 0 2 2 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 1 0 0
1 1 1 1 0 0
Thought: We want to place it in the bottom right corner, so we need its distance from the left to be 4. We also do not need to rotate it, rotation is Static, and our operation is Static 4.
Operation: Static 4
Status after operation:
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 1 1 1
1 1 1 1 1 1
Status after scoring:
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 1 1 1

Status:
0 2 2 2 2 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 1 1
0 0 1 0 1 1
1 1 1 0 1 1
1 1 1 0 1 1
Thought: At present, only the fourth column requires a block, and it needs to be vertical. Therefore, we need to rotate it and place it on the fourth column, which means a rotation operation with a distance of 3 from the left boundary.
Operation: Rotate 3
Status after operation:
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 1 1 1
0 0 1 1 1 1
0 0 1 1 1 1
1 1 1 1 1 1
Status after scoring:
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 1 1 1
0 0 1 1 1 1

Status:
0 0 2 2 0 0
0 0 2 2 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 1 1 1
0 0 1 1 1 1
Thought: At present, the first two column requires a block. Therefore, we do not need to rotate it and place it on the first column, which means a static operation with a distance of 0 from the left boundary.
Operation: Static 0
Status after operation:
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
1 1 1 1 1 1
1 1 1 1 1 1
Status after scoring:
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
"""
