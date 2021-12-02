

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


def test_evaluate_nulle():
    # Vérifie une partie nulle
    players: List[Player] = [AI('X'), Human('O')]
    board: List = [
        [players[X], players[O], players[X]],
        [players[O], players[X], players[O]],
        [players[O], players[X], players[O]]
        ]
    game: TicTacToe = TicTacToe(None, True)
    game.players = players
    assert game.evaluate(board) == 0


def test_evaluate1_O_gagnant():
    # Humain Gagne
    players: List[Player] = [AI('X'), Human('O')]
    board: List = [
        [players[X], players[O], players[X]],
        [players[O], players[O], players[O]],
        [players[O], players[X], players[X]]
        ]
    game: TicTacToe = TicTacToe(None, True)
    game.players = players
    assert game.evaluate(board) == -10


def test_evaluate2_X_gagnant():
    # AI Gagne
    players: List[Player] = [AI('X'), Human('O')]
    board: List = [
        [players[X], players[X], players[X]],
        [players[O], players[O], players[X]],
        [players[X], players[X], players[O]]
        ]
    game: TicTacToe = TicTacToe(None, True)
    game.players = players

    assert game.evaluate(board) == 10


def test_evaluate_depth():

    game: TicTacToe = TicTacToe(None, True)
    game.players = [AI('X'), Dummy('O')]
    before = time.time()
    game.next_player = game.players[X]
    dure_time = time.time() - before
    print(dure_time)
    move: tuple = game.next_player.play_depth(game, game.initial)

    assert move == (0, 0)


def test_evaluate_pruning():

    game: TicTacToe = TicTacToe(None, True)
    game.players = [AI('X'), Dummy('O')]
    game.next_player = game.players[X]
    before = time.time()
    move: tuple = game.next_player.play_pruning(game, game.initial)
    dure_time = time.time() - before
    print('durée:', dure_time)
    assert move == (0, 0)

