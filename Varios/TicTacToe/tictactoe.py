"""
Tic Tac Toe Player
"""

import math
import random
import numpy as np

X = 'X'
O = 'O'
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(user, board):
    """
    Returns player who has the next turn on a board.
    """
    contX = 0
    contO = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 'X':
                contX+=1
            if board[i][j] == 'O':
                contO+=1

    if (contX == contO):
        return X
    if (contX > contO):
        return O
    if (contX < contO):
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    listActions = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                listActions.append((i,j))

    return listActions


def result(user,board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j=action
    board[i][j]=player(user,board)
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if utility(board) == 1:
        return X
    elif utility(board) == -1:
        return O
    else:
        return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    else:
        contEmp=0
        for i in range(len(board)):
            for j in range(len(board)):
                if (board[i][j] == X or board[i][j] == O):
                    contEmp+=1
        if (contEmp == 9 ):
            return True


    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    end = False
    ficha = ['X','O']
    value = [1,-1]
    cont=0
    while (cont<2):
        contD1 = 0
        contD2 = 0
        contEmp = 0
        contF = 0
        contC = 0
        i = 0
        for i in range(len(board)):
            contC = 0
            contF = 0
            j = 0
            for j in range(len(board)):
                if (i == j) and ((board[i][j]) == ficha[cont]):
                    contD1+=1
                if ((i + j) == 2 and (board[i][j]) == ficha[cont]):
                    contD2+=1
                if (board[i][j] == X or board[i][j] == O):
                    contEmp+=1
                if (board[i][j] == ficha[cont]):
                    contF+=1
                    if (contF == 3):
                        end = value[cont]
                if (board[j][i] == ficha[cont]):
                    contC+=1
                    if (contC == 3):
                        end = value[cont]

        if (contD1 == 3):
            end = value[cont]
        if (contD2 == 3):
            end = value[cont]
        if (contEmp == 9 and end == False):
            end = 0
        cont+=1
    if not end:
        end = 0

    return end



def minimax(user,board):
    """
    Returns the optimal action for the current player on the board.
    """
    optimalAction = []
    for action in actions(board):
        aux = np.copy(board)
        aux[action[0]][action[1]] = player(user, board)
        pierde = False
        if winner(aux) == user:
                return action
        else:
            for action1 in actions(aux):
               aux1 = np.copy(aux)
               aux1[action1[0]][action1[1]] = player(user, aux)
               if  winner(aux1) == player(user,aux):
                   pierde = True
                   break
               if pierde == False:
                  for action2 in actions(aux1):
                      aux2 = np.copy(aux1)
                      aux2[action2[0]][action2[1]] = player(user, aux2)
                      if  winner(aux2) == player(user,aux2):
                        pierde = True


        if pierde == False:
            optimalAction.append(action)


    if len(optimalAction) > 0:
        return optimalAction[random.randint(0, len(optimalAction) -1)]

    return actions(board)[random.randint(0, len(actions(board)) -1)]

