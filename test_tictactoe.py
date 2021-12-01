

from player import Player
from tictactoe import TicTacToe
from human import Human
from dummy import Dummy
from ai import AI
from typing import List
from constants import X, O
import time


MAX = 1
MIN = -1


def test_evaluate():
    # Vérifie une partie nulle
    players: List[Player] = [AI('X'), Human('O')]
    board = [
        [players[X], players[O], players[X]],
        [players[O], players[X], players[O]],
        [players[X], players[O], players[X]]
        ]
    game: TicTacToe = TicTacToe()
    game.players = players
    assert game.evaluate(board) == 1


# def test_evaluate1_O_gagnant():
    # Humain Gagne
    # players: List[Player] = [AI('X'), Human('O')]
    # board: List = [
    #     [players[X], players[O], players[X]],
    #     [players[O], players[O], players[O]],
    #     [players[O], players[X], players[X]]
    #     ]
    # game: TicTacToe = TicTacToe()
    # game.evaluate(board)
    # game.players = players
    # assert game.evaluate(board) is 1
        
        
# def test_evaluate2_X_gagnant():
    # AI Gagne
    # players: List[Player] = [AI('X'), Human('O')]
    # board: List = [
    #     players[X], players[X], players[X],
    #     players[O], players[O], players[X],
    #     players[X], players[X], players[O]
    #     ]
    # game: TicTacToe = TicTacToe()
    # game.evaluate(board)
    # game.players = players
    # assert game.evaluate(board) is -1

# def test_evaluate_depth():
#     # Vérifie une partie nulle
#     players: List[Player] = [AI('X'), Human('O')]
#     board = [
#         [None, None, None],
#         [None, None, None],
#         [None, None, None]
#     ]
#     before = time.time()
#     pos = game.play_depth()
#     # game: TicTacToe = TicTacToe()
#     game.players = players
#     duretime = time.time() - before
#     print('durée:', duretime)
#     assert game.evaluate(board) == 1

def test_evaluate_depth():

    game: TicTacToe = TicTacToe(None, True)
    game.players = [AI('X'), Dummy('O')]
    game.next_player = game.players[X]
    move: tuple = game.next_player.play(game, game.initial)

    assert move == (0, 0)
