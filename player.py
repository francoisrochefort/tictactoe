

from typing import List
from abc import ABC


class Player(ABC):
    def play(self, game: 'Game', state: List) -> tuple:
        pass
    

