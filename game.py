
from __future__ import annotations
from typing import List
from player import Player


class Game:
    """A game is similar to a problem, but it has a utility for each
    state and a terminal test instead of a path cost and a goal
    test. To create a game, subclass this class and implement actions,
    result, utility, and terminal_test. You may override display and
    successors or you can inherit their default methods. You will also
    need to set the .initial attribute to the initial state; this can
    be done in the constructor."""

    def __init__(self, initial: 'State'):
        """The constructor specifies the initial state,
        Your subclass's constructor can add
        other arguments."""
        self.initial: 'State' = initial

    def actions(self, state: 'State') -> List['Action']:
        """Return a list of the allowable moves at this point."""
        raise NotImplementedError

    def result(self, state: 'State', move: 'Action') -> 'State':
        """Return the state that results from making a move from a state."""
        raise NotImplementedError

    def utility(self, state: 'State', player):
        """Return the value of this final state to player."""
        raise NotImplementedError

    def terminal_test(self, state: 'State') -> bool:
        """Return True if this is a final state for the game. ie. no moves form here"""
        return not self.actions(state)

    def to_move(self, state: 'State') -> str:
        """Return the player description whose move it is in this state."""
        raise NotImplementedError

    def display(self, state: List):
        """Print or otherwise display the state."""
        print('**********************************')
        for row in state:
            print(str(row[0]) + '\t\t', str(row[1]) + '\t\t', str(row[2]))

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    def play_game(self, players: List[Player]):
        state: List = self.initial
        while True:
            for player in players:
                move: tuple = player.play(self, state)
                state = self.result(state, move)
                if self.terminal_test(state):
                    self.display(state)
                    return self.utility(state, self.to_move(self.initial))

