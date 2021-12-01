# tictactoe
project final du cours d'inlteligence artificielle 2

Explication de l'ajout de  profondeur:
Making our AI smarter :

One final step is to make our AI a little bit smarter. Even though the following AI plays perfectly, it might choose to make a move which will result in a slower victory or a faster loss. Lets take an example and explain it.
Assume that there are 2 possible ways for X to win the game from a give board state.

    Move A : X can win in 2 move
    Move B : X can win in 4 moves

Our evaluation function will return a value of +10 for both moves A and B. Even though the move A is better because it ensures a faster victory, our AI may choose B sometimes. To overcome this problem we subtract the depth value from the evaluated score. This means that in case of a victory it will choose a the victory which takes least number of moves and in case of a loss it will try to prolong the game and play as many moves as possible. So the new evaluated value will be

    Move A will have a value of +10 – 2 = 8
    Move B will have a value of +10 – 4 = 6

Now since move A has a higher score compared to move B our AI will choose move A over move B. The same thing must be applied to the minimizer. Instead of subtracting the depth we add the depth value as the minimizer always tries to get, as negative a value as possible. We can subtract the depth either inside the evaluation function or outside it. Anywhere is fine. I have chosen to do it outside the function. Pseudocode implementation is as follows. 

if maximizer has won:
    return WIN_SCORE – depth

else if minimizer has won:
    return LOOSE_SCORE + depth


Référence:
https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/
