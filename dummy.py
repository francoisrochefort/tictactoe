
from typing import List
from player import Player


class Dummy(Player):

    def __init__(self, name: str):
        self.name: str = name

    def __eq__(self, other):
        return isinstance(other, str) and self.name == other.name

    def play(self, game: 'Game', state: List) -> tuple:
        pass
