"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
from math import inf

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
           
    
def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for i in board:
        for j in i:
            if j == None:
                count += 1
    if count % 2 == 1:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                actions.add((i,j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    who = player(board)
    new_board = deepcopy(board)
    if action in actions(board):
        new_board[action[0]][action[1]] = who
        return new_board
    raise ValueError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if (board[i][0]==board[i][1] == board[i][2] and board[i][0] != None):
            return board[i][0]
        if (board[0][i] == board[1][i] == board[2][i] and board[0][i] != None):
            return board[0][i]

    if (board[0][0]==board[1][1] == board[2][2] and board[0][0] != None):
        return board[0][0]
    if (board[0][2]==board[1][1] == board[2][0] and board[0][2] != None):
        return board[0][2]

    return None
            
            
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or not any(None in sublist for sublist in board):
        return True

    return False
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        t = - inf
        for a in actions(board):
            v = min_value(result(board, a))
            if v > t:
                best_action = a
                t = v
        return best_action

    t = inf
    for a in actions(board):
        v = max_value(result(board, a))
        if v < t:
            best_action = a
            t = v
    return best_action



def max_value(board):
    if terminal(board):
        return utility(board)

    v = - inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)

    v = inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v



if __name__ == "__main__":
    print(utility(initial_state()))