# Minimax Tic Tac Toe
### Projet final du cours d'intelligence artificielle 2

## 1) L'algorythme utilisé:  
Minimax pour un jeu d'adversaire. Le jeu utilisé est TicTacToe.
voici la ressource pour le dataframe utilisé:

https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/

## 2) Performance 
L'algorythme Minimax est très performant pour les jeux à deux adversaires, Le tictactoe étant un jeux avec peu d'états finaux, il est assez simple de rechercher la meilleure position à jouer.  Si le jeux est plus complexe, il doit être utilisé avec la methode alpha-beta pruning pour permettre d'aller plus loin dans l'estimation de la meilleur action à prendre.

Nous avons ajouté des fonctions avec la profendeur et avec le alpha beta pruning, pour ajouter des tests de perfromance.


## 3) Profondeur
Explication de l'ajout de  profondeur:

    Making our AI smarter :

    One final step is to make our AI a little bit smarter. Even though the following AI plays perfectly, it might choose to make a move which will result in a slower victory or a faster loss. Lets take an example and explain it.
    Assume that there are 2 possible ways for X to win the game from a give board state.

        Move A : X can win in 2 move
        Move B : X can win in 4 moves

    So the new evaluated value will be

        Move A will have a value of +10 - 2 = 8
        Move B will have a value of +10 - 4 = 6

    plementation is as follows. 

        if maximizer has won:
            return WIN_SCORE - depth

        else if minimizer has won:
            return LOOSE_SCORE + depth


## 4) Références:

Le fichier orienté objet est ai.py, contient la classe qui fait jouer le AI, en utilisant l'algorythme Minimax pour déterminer le meilleur endroit pour jouer.  

https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/



Voici mon lien pour l'explication du pruning, il y a aussi l'Example du DEEP CUT OFF que je vous ai mentionné.

https://youtu.be/STjW3eH0Cik?t=1283


