import re
import random
import logging
from typing import List
from openai import OpenAI
from langchain.prompts import PromptTemplate
from prompts import cot_agent_prompt

class CoTAgent:
    def __init__(self, game,
                client: OpenAI,
                rules: str,
                cot_examples: str,
                agent_prompt: PromptTemplate = cot_agent_prompt,
                ):
        self.model = ''
        self.game = game
        self.rules = rules
        self.cot_examples = cot_examples
        self.agent_prompt = agent_prompt
        self.client = client
        self.step_n: int = 0
        self.scratchpad: str = ''
        self.scratchpads: List[str] = []

    def chat(self, prompt):
        while True:
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                )
                logging.info(response)
                return response.to_dict()['choices'][0]['message']['content']
            except:
                continue

    def step_2048(self):
        self.step_n += 1
        self.scratchpad += f'\nThought:'
        self.status = self.game.get_status()
        thought = self.prompt_agent()
        logging.info(f"Thought: {thought}")
        self.scratchpad += ' ' + thought
        direction = find_direction(thought.lower())
        logging.info(f"Operation: {direction}")
        self.scratchpads.append(self.scratchpad)
        self.scratchpad = ""

        return self.game.step(direction)

    def step_2048_random(self):
        self.step_n += 1
        direction = random.choice(['up', 'down', 'left', 'right'])
        return self.game.step(direction)

    def step_snake(self):
        self.step_n += 1
        self.scratchpad += f'\nThought:'
        self.status = self.game.get_status()
        thought = self.prompt_agent()
        logging.info(f"Thought: {thought}")
        self.scratchpad += ' ' + thought
        direction = find_direction(thought.lower())
        number = int(find_number(thought))
        logging.info(f"Operation: {direction} {number}")
        self.scratchpads.append(self.scratchpad)
        self.scratchpad = ""

        return self.game.step(direction, number)

    def step_snake_random(self):
        self.step_n += 1
        direction = random.choice(['up', 'down', 'left', 'right'])
        number = random.randint(1, 7)
        return self.game.step(direction, number)

    def step_tetris(self):
        self.step_n += 1
        self.scratchpad += f'\nThought:'
        self.status = self.game.get_status()
        thought = self.prompt_agent()
        logging.info(f"Thought: {thought}")
        self.scratchpad += ' ' + thought
        operation = find_operation(thought.lower())
        number = int(find_number(thought))
        logging.info(f"Operation: {operation} {number}")
        self.scratchpads.append(self.scratchpad)
        self.scratchpad = ""
        rotation = {"static": 0, "rotate": 1}[operation]

        return self.game.step(number, rotation)

    def step_tetris_random(self):
        self.step_n += 1
        direction = random.choice(['rotate', 'down', 'left', 'right'])
        number = random.randint(1, 7)
        return self.game.step(direction, number)

    def prompt_agent(self) -> str:
        return format_step(self.chat(self._build_agent_prompt()))

    def _build_agent_prompt(self) -> str:
        return self.agent_prompt.format(
                            rules = self.rules,
                            examples = self.cot_examples,
                            status = self.status,
                            scratchpad = self.scratchpad)

def format_step(step: str) -> str:
    return step.strip('\n').strip().replace('\n', '')

def find_direction(text):
    return max(['up', 'down', 'left', 'right'], key=text.rfind)

def find_operation(text):
    return max(['rotate', 'static'], key=text.rfind)

def find_number(text):
    return re.search(r'(\d+)(\D*)$', text).group(1)
