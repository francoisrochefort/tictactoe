
from player import Player
from typing import List
import random
import pygame
from constants import *


class Human(Player):

    def __init__(self, name: str):
        self.name = name

    def hit_test(self) -> tuple:
        # get coordinates of mouse click
        # retourne l''index de la POSITIONS 0 à 8
        x, y = pygame.mouse.get_pos()

        # get column of mouse click (1-3)
        if x < WIDTH / 3:
            col = 1
        elif x < WIDTH / 3*2:
            col = 2
        elif x < WIDTH:
            col = 3
        else:
            col = None

        # get row of mouse click (1-3)
        if (y < HEIGHT / 3):
            row = 1

        elif (y < HEIGHT / 3 * 2):
            row = 2

        elif (y < HEIGHT):
            row = 3

        else:
            row = None
        # after getting the row and col,
        # we need to draw the images at
        # the desired positions
        row -= 1
        col -= 1
        if row is not None and col is not None:
                if row == 0 and col == 0: index = 0
                elif row == 0 and col == 1:
                    index = 1
                elif row == 0 and col == 2:
                    index = 2
                elif row == 1 and col == 0:
                    index = 3
                elif row == 1 and col == 1:
                    index = 4
                elif row == 1 and col == 2:
                    index = 5
                elif row == 2 and col == 0:
                    index = 6
                elif row == 2 and col == 1:
                    index = 7
                elif row == 2 and col == 2:
                    index = 8
                else:
                    return (-1, -1) #'Invalid CLick'
        return (col, row)
         
    # return  random.choice(game.actions(state))
    def play(self, game: "Game", state: List) -> tuple:
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return self.hit_test()
            pygame.display.update()
    pygame.quit()

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, Human) and self.name == other.name
