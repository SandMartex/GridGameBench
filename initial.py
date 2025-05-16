import random
import datetime
import numpy as np
from openai import OpenAI

def merge(b):
    if np.all(b == 0):
        return b
    if b[0] == 0:
        b[0:3] = b[1:]
        b[3] = 0
    if b[0] == 0:
        b[0:3] = b[1:]
        b[3] = 0
    if b[0] == 0:
        b[0:3] = b[1:]
        b[3] = 0
    if b[1] == 0:
        b[1:3] = b[2:]
        b[3] = 0
    if b[1] == 0:
        b[1:3] = b[2:]
        b[3] = 0
    if b[2] == 0:
        b[2] = b[3]
        b[3] = 0
    if b[0] == b[1]:
        b[0] = b[0] + b[1]
        b[1:3] = b[2:]
        b[3] = 0
    if b[1] == b[2]:
        b[1] = b[1] + b[2]
        b[2] = b[3]
        b[3] = 0
    if b[2] == b[3]:
        b[2] = b[2] + b[3]
        b[3] = 0
    return(b)

def left(a):
    a[0] = merge(a[0])
    a[1] = merge(a[1])
    a[2] = merge(a[2])
    a[3] = merge(a[3])
    return a

def right(a):
    a[0] = merge(a[0][::-1])[::-1]
    a[1] = merge(a[1][::-1])[::-1]
    a[2] = merge(a[2][::-1])[::-1]
    a[3] = merge(a[3][::-1])[::-1]
    return a

def up(a):
    a[:,0] = merge(a[:,0])
    a[:,1] = merge(a[:,1])
    a[:,2] = merge(a[:,2])
    a[:,3] = merge(a[:,3])
    return a

def down(a):
    a[:,0] = merge(a[:,0][::-1])[::-1]
    a[:,1] = merge(a[:,1][::-1])[::-1]
    a[:,2] = merge(a[:,2][::-1])[::-1]
    a[:,3] = merge(a[:,3][::-1])[::-1]
    return a

def new(a):
    indices = np.where(a == 0)
    if indices[0].size == 0:
        return
    random_index = np.random.choice(indices[0].size)
    selected_row = indices[0][random_index]
    selected_col = indices[1][random_index]

    if random.random() > .5:
        a[selected_row, selected_col] = 2
    else:
        a[selected_row, selected_col] = 4
    return a

def play(a, dir):
    if dir == 'left':
        b = left(a)
    if dir == 'right':
        b = right(a)
    if dir == 'up':
        b = up(a)
    if dir == 'down':
        b = down(a)
    b = new(b)
    return b

def text(a):
    matrix_text = "\n".join([" ".join(map(str, row)) for row in a])
    return matrix_text

# rule = "Hello, let's play a game, called 2048. Here I will provide you with a 4 * 4 matrix, and you can and only can response [left, right, up, down], then the matrix will move as you say, when two identical number meets each other, they will merge and become double. There is ONLY your turn, no my turn. Do not tell me what it looks like after move, which is decided by a program. Your goal is to get larger number. Your score is the sum of all the numbers when you can not move."

rule = "Hello, let's play a game, called 2048. For each step, I will provide you with a 4 * 4 matrix, and you should response with UPPER all around word such as [**UP**, **DOWN**, **LEFT**, **RIGHT**], then the matrix will move as you say. Your goal is to have highest score, and your score is the sum of all the numbers when you can not move."


def chat_with_gpt(client, a):
    full_prompt = "\n\n".join([rule, "The status now is: ", text(a)])
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": full_prompt}],
    )
    txt = response.to_dict()['choices'][0]['message']['content']
    return txt

if __name__ == "__main__":
    client = OpenAI()

    N = 10
    results = np.zeros((N))
    for i in range(N):
        a = np.zeros((4, 4))
        a[1, 1] = 2
        a[2, 2] = 4
        history = rule
        name = "record/" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.txt")
        while True:
            history = history + "\n\n" + text(a)
            thought = chat_with_gpt(client, a)
            action = ""
            for act in ["**LEFT**", "**RIGHT**", "**UP**", "**DOWN**"]:
                if act in thought:
                    action = act[2: -2].lower()
            history = history + "\n\n" + action
            print(action)
            if action:
                a = play(a, action)
                if not isinstance(a, np.ndarray):
                    break
            else:
                break
        results[i] = np.sum(a)
        with open(name, 'w') as file:
            file.write(history)
    result_name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S_result.txt")
    with open(result_name, 'w') as file:
        file.write(" ".join(results.tolist()))
