

from player import Player
from tictactoe import TicTacToe
from human import Humain
from ai import AI
from typing import List
from constants import X, O


MAX = 1
MIN = -1


def test_evaluate():
    # tie
    players: List[Player] = [AI('X'), Humain('O')]
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
    # players: List[Player] = [AI('X'), Humain('O')]
    # board: List = [
    #     [players[X], players[O], players[X]],
    #     [players[O], players[O], players[O]],
    #     [players[O], players[X], players[X]]
    #     ]
    # game: TicTacToe = TicTacToe()
    # game.evaluate(board)
    # game.players = players
    # assert game.evaluate(board) is 1
        
        
# def test_evaluate2_X_gagnang():        
    # AI Gagne
    # players: List[Player] = [AI('X'), Humain('O')]
    # board: List = [
    #     players[X], players[X], players[X],
    #     players[O], players[O], players[X],
    #     players[X], players[X], players[O]
    #     ]
    # game: TicTacToe = TicTacToe()
    # game.evaluate(board)
    # game.players = players
    # assert game.evaluate(board) is -1
    
    
    
    
    
    
    