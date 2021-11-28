

from typing import List
from constants import ROWS, COLS, X, O
from player import Player


class AI(Player):

    def __init__(self, name: str):
        self.name: str = name

    def __eq__(self, other):
        return isinstance(other, str) and self.name == other.name

    def minimax(self, game: 'Game', state: List, is_max) -> int:

        # if either the maximizing or the minimizing wins then return the score
        score: int = game.evaluate(state)
        if score != 0:
            return score

        # there is no more possible move and no winner; it is a tie
        if len(game.actions(state)) == 0:
            return 0

        # maximizing player
        if is_max:

            score = - 2
            for row in range(ROWS):
                for col in range(COLS):
                    if state[row][col] is None:
                        state[row][col] = game.players[X]
                        score = max(self.minimax(game, state, False), score)
                        state[row][col] = None
            return score

        # minimizing player
        else:

            score = 2
            for row in range(ROWS):
                for col in range(COLS):
                    if state[row][col] is None:
                        state[row][col] = game.players[O]
                        score = min(self.minimax(game, state, True), score)
                        state[row][col] = None
            return score

    def play(self, game: 'Game', state: List) -> tuple:

        best: int = -2
        move: tuple = None

        for row in range(ROWS):
            for col in range(COLS):

                if state[row][col] is None:

                    # move and evaluate
                    state[row][col] = game.players[X]
                    value = self.minimax(game, state, False)
                    state[row][col] = None

                    # keep the best move
                    if value > best:
                        move = (col, row)
                        best = value

        return move

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, AI) and self.name == other.name
