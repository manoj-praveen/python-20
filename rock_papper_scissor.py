import random
import sys
from typing import Final

ROCK: Final[str] = 'rock'
PAPER: Final[str] = 'paper'
SCISSOR: Final[str] = 'scissor'
EXIT: Final[str] = 'exit'


class RPS:

    def __init__(self):
        print("Welcome to Rock, Paper & Scissors")
        self.moves: dict = {'rock': '🪨', 'paper': '📃', 'scissor': '✂️'}

    def keep_playing(self) -> None:
        user_choice: str = input("Enter rock or paper or scissor:").lower()
        if user_choice == EXIT:
            print('Thanks for Playing!!')
            sys.exit()
        if user_choice not in [ROCK, PAPER, SCISSOR]:
            print("Please provide a valid choice: [rock or paper or scissor]")
            return

        ai_choice = random.choice(list(self.moves.keys()))
        print(f'user choice: {self.moves.get(user_choice)}')
        print(f'AI choice: {self.moves.get(ai_choice)}')

        if user_choice == ROCK and ai_choice == PAPER:
            print('AI win')
        elif user_choice == ROCK and ai_choice == SCISSOR:
            print('You win')
        elif user_choice == PAPER and ai_choice == ROCK:
            print('You win')
        elif user_choice == PAPER and ai_choice == SCISSOR:
            print('AI win')
        elif user_choice == SCISSOR and ai_choice == ROCK:
            print('AI win')
        elif user_choice == SCISSOR and ai_choice == PAPER:
            print('You win')
        else:
            print('Tie')


if __name__ == '__main__':
    rps = RPS()

    while True:
        rps.keep_playing()
