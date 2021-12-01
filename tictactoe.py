

from game import Game
from typing import List, Optional
from player import Player
from constants import *
from ai import AI
from human import Human
import pygame
import os


class TicTacToe(Game):

    def __init__(self, initial: List = None):

        # init. players attribute
        self.players: Optional[List[Player]] = None
        self.next_player = None

        # init. the board
        if not initial:
            self.initial = [[None for _ in range(COLS)] for _ in range(ROWS)]
        super().__init__(self.initial)

        # init.the user interface
        self.create_window()
        self.draw_background()
    
    def create_window(self):
        pygame.font.init()
        pygame.init()
        self.win = pygame.display.set_mode((WIDTH, HEIGHT_tot))
        pygame.display.set_caption("MINIMAX - TicTacToe")

    def draw_move(self, player, move):
        if isinstance(player, Human):
            self.win.blit(YELLOW_O, (move.y, move.x))
        else:
            self.win.blit(RED_X, (move.y, move.x))
        pygame.display.update()

    def index_of(self, pos: tuple) -> int :
        return (pos[1] * COLS) + pos[0]

    def draw_background(self):

        self.win.fill(WHITE)
        self.win.blit(BACK_GROUND, (0, 0))
        pygame.draw.line(self.win, WHITE, (WIDTH / 3, 0), (WIDTH / 3, HEIGHT), 7)
        pygame.draw.line(self.win, WHITE, (WIDTH / 3 * 2, 0), (WIDTH / 3 * 2, HEIGHT), 7)
        pygame.draw.line(self.win, WHITE, (0, HEIGHT / 3), (WIDTH, HEIGHT / 3), 7)
        pygame.draw.line(self.win, WHITE, (0, HEIGHT / 3 * 2), (WIDTH, HEIGHT / 3 * 2), 7)
        pygame.display.update()

    def draw_board(self, state: List):
        for row in range(ROWS):
            for col in range(COLS):
                if state[row][col] is not None:
                    index = self.index_of((row, col))
                    poh = pygame.Rect(POSITIONS[index][0], POSITIONS[index][1], XO_WIDTH, XO_HEIGHT)
                    self.draw_move(state[row][col], poh)
        pygame.display.update()

    def actions(self, state: List) -> List[tuple]:

        # list all possible moves
        moves: List[(int, int)] = []
        for row in range(ROWS):
            for col in range(COLS):
                if state[row][col] is None:
                    moves.append((row, col))
        return moves

    def result(self, state: List, move: tuple) -> List:

        # perform the move
        state[move[1]][move[0]] = self.next_player

        # set the next player
        self.next_player = self.players[X] if self.next_player == self.players[O] else self.players[O]

        # update user interface        
        self.draw_board(self.initial)

        return state

    def evaluate(self, state: List) -> int:

        # horizontal
        for row in range(ROWS):
            if state[row][0] == state[row][1] and state[row][1] == state[row][2]:
                if state[row][0] == self.players[X]:
                    return 1
                elif state[row][0] == self.players[O]:
                    return -1

        # vertical
        for col in range(COLS):
            if state[0][col] == state[1][col] and state[1][col] == state[2][col]:
                if state[0][col] == self.players[X]:
                    return 1
                elif state[0][col] == self.players[O]:
                    return -1

        # diagonal #1
        if state[0][0] == state[1][1] and state[1][1] == state[2][2]:
            if state[0][0] == self.players[X]:
                return 1
            elif state[0][0] == self.players[O]:
                return -1

        # diagonal #2
        if state[0][2] == state[1][1] and state[1][1] == state[2][0]:
            if state[0][2] == self.players[X]:
                return 1
            elif state[0][2] == self.players[O]:
                return -1

        # tie
        return 0

    def terminal_test(self, state: List) -> bool:

        # terminate if one of the two players has won the game
        result: int = self.evaluate(state)
        if result == 1 or result == -1:
            return True

        # also terminate if the game is a tie
        return True if len(self.actions(state)) == 0 else False

    def utility(self, state: List, player: Player):
        pass

    def to_move(self, state: List):
        pass

    def play_game(self, players: List[Player]):

        # set the player list
        self.players = players

        # set the first player to play
        self.next_player = self.players[X]

        # begin the game
        super().play_game(players)

        # wait for the user to press any key
        done: bool = False 
        while not done: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    done = True


if __name__ == '__main__':

    while True:
        game: TicTacToe = TicTacToe()
        game.play_game([AI('X'), Human('O')])
