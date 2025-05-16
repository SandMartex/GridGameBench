import os
import logging
import datetime
import numpy as np
from openai import OpenAI
from agents import CoTAgent
from game2048 import Game2048
from gamesnake import GameSnake
from gametetris import GameTetris
from fewshots import RULES_2048, COT_2048
from fewshots import RULES_SNAKE, COT_SNAKE
from fewshots import RULES_TETRIS, COT_TETRIS

def log_config(folder, name):
    current_time = datetime.datetime.now()
    time_str = current_time.strftime("%Y%m%d_%H%M%S") + '_' + name
    log_file_path = os.path.join(folder, f'{time_str}.log')

    if '_' in name:
        logging.basicConfig(
            filename=log_file_path,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s\n%(message)s'
        )
    else:
        logging.basicConfig(
            filename=log_file_path,
            level=logging.CRITICAL,
            format='%(asctime)s - %(levelname)s\n%(message)s'
        )
    return log_file_path

def play(title, name, model):
    if name == 'openai':
        client = OpenAI()
    elif name == 'deepseek':
        client = OpenAI(api_key="Your_API_Key", base_url="https://api.deepseek.com/v1")
    if '2048' in title:
        game = Game2048(4)
        agent = CoTAgent(game, client, RULES_2048, COT_2048)
    elif 'Snake' in title:
        game = GameSnake(8)
        agent = CoTAgent(game, client, RULES_SNAKE, COT_SNAKE)
    elif 'Tetris' in title:
        game = GameTetris(8, 6)
        agent = CoTAgent(game, client, RULES_TETRIS, COT_TETRIS)
    agent.model = model
    step_n = 512
    status_list = []
    for _ in range(step_n):
        if title == '2048':
            grid, score, status = agent.step_2048()
        elif title == '2048_random':
            grid, score, status = agent.step_2048_random()
        elif title == 'Snake':
            grid, score, status = agent.step_snake()
        elif title == 'Snake_random':
            grid, score, status = agent.step_snake_random()
        elif title == 'Tetris':
            grid, score, status = agent.step_tetris()
        elif title == 'Tetris_random':
            grid, score, status = agent.step_tetris_random()
        logging.info(grid)
        logging.info(score)
        logging.info(status)
        status_list.append(status)
        if status == "over" or status == "dead":
            break
    logging.info(f"Final Score is: {game.score}")
    logging.info(f"Final Round is: {len(status_list)}")
    logging.info(f"Valid Round is: {status_list.count("actv") + 1}")
    logging.info(f"Valid Rate is: {(status_list.count("actv") + 1) / len(status_list)}")
    return game.score, len(status_list), status_list.count("actv") + 1, (status_list.count("actv") + 1) / len(status_list)


def main(title, name, model, reps):
    if '_' in title:
        fname = log_config(title.split('_')[0], f'{reps}')
    else:
        fname = log_config(title, f'{name}_{model}_{reps}')
    logging.critical(f"Starts with {reps} {title} games, using {name} {model}")
    data = np.zeros((reps, 4))
    for i in range(reps):
        data[i] = play(title, name, model)
        logging.critical(f"Finish {i+1} games!!")
        np.savetxt(fname + '.csv', data, delimiter=',', fmt='%d, %d, %d, %.4f')
    logging.critical(f"Score: {np.average(data[:, 0])} ± {np.std(data[:, 0])}")
    logging.critical(f"Round: {np.average(data[:, 1])} ± {np.std(data[:, 1])}")
    logging.critical(f"Valid: {np.average(data[:, 3])} ± {np.std(data[:, 3])}")
    if reps >= 100:
        data = np.sort(data, axis=0)
        logging.critical(f"Highest Score: {data[-10:, 0]}")
        logging.critical(f"Lowest Score : {data[ :10, 0]}")
        logging.critical(f"Highest Round: {data[-10:, 1]}")
        logging.critical(f"Lowest Round : {data[ :10, 1]}")
        logging.critical(f"Highest Valid: {data[-10:, 2]}")
        logging.critical(f"Lowest Valid : {data[ :10, 2]}")
        logging.critical(f"Valid Rate   : {np.sum(data[:, 3]) / np.sum(data[:, 1])}")

if __name__ == "__main__":
    main('2048', 'openai', 'gpt-3.5-turbo', 100)
    main('Snake', 'openai', 'gpt-3.5-turbo', 100)
    main('Tetris', 'openai', 'gpt-3.5-turbo', 100)
