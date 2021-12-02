
from typing import List
from constants import ROWS, COLS, X, O, MINFINITY, MAXFINITY
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

    def play_depth(self, game: 'Game', state: List) -> tuple:

        best: int = -1000
        move: tuple = None

        for row in range(ROWS):
            for col in range(COLS):

                if state[row][col] is None:

                    # move and evaluate
                    state[row][col] = game.players[X]
                    value = self.minimax_depth(game, 0, state, False)
                    state[row][col] = None

                    # keep the best move
                    if value > best:
                        move = (col, row)
                        best = value

        return move

    def minimax_depth(self, game: 'Game', depth: int, state: List, is_max) -> int:

        # if either the maximizing or the minimizing wins then return the score
        winner: int = game.evaluate(state)
        if winner != 0:
            if is_max:
                score = winner - depth
            else:
                score = winner + depth
            return score

        # there is no more possible move and no winner; it is a tie
        if len(game.actions(state)) == 0:
            return 0

        # maximizing player
        if is_max:
            score = -1000
            for row in range(ROWS):
                for col in range(COLS):
                    if state[row][col] is None:
                        state[row][col] = game.players[X]
                        score = max(self.minimax_depth(game, depth+1, state, False), score)
                        state[row][col] = None
            return score

        # minimizing player
        else:
            score = 1000
            for row in range(ROWS):
                for col in range(COLS):
                    if state[row][col] is None:
                        state[row][col] = game.players[O]
                        score = min(self.minimax_depth(game, depth+1, state, True), score)
                        state[row][col] = None
            return score

    def play_pruning(self, game: 'Game', state: List) -> tuple:

        best: int = -1000
        move: tuple = None

        for row in range(ROWS):
            for col in range(COLS):

                if state[row][col] is None:

                    # move and evaluate
                    state[row][col] = game.players[X]
                    value = self.minimax_ab_prune(game, 0, state, False, MINFINITY, MAXFINITY)
                    state[row][col] = None

                    # keep the best move
                    if value > best:
                        move = (col, row)
                        best = value

        return move

    def minimax_ab_prune(self, game: 'Game', depth: int, state: List, is_max, alpha, beta) -> int:

        # if either the maximizing or the minimizing wins then return the score
        winner: int = game.evaluate(state)
        if winner != 0:
            if is_max:
                score = winner - depth
            else:
                score = winner + depth
            return score

        # there is no more possible move and no winner; it is a tie
        if len(game.actions(state)) == 0:
            return 0

        # maximizing player
        if is_max:
            score = MINFINITY
            for row in range(ROWS):
                for col in range(COLS):
                    if state[row][col] is None:
                        state[row][col] = game.players[X]
                        score = max(self.minimax_ab_prune(game, depth+1, state, False, alpha, beta), score)
                        state[row][col] = None
                        alpha = max(alpha, score)

                        # Alpha Beta Pruning
                        if beta >= alpha:
                            break
            return score

        # minimizing player
        else:
            score = MAXFINITY
            for row in range(ROWS):
                for col in range(COLS):
                    if state[row][col] is None:
                        state[row][col] = game.players[O]
                        score = min(self.minimax_ab_prune(game, depth+1, state, True, alpha, beta), score)
                        state[row][col] = None
                        beta = min(beta, score)

                        # Alpha Beta Pruning
                        if beta <= alpha:
                            break
            return score

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, AI) and self.name == other.name
