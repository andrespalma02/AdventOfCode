"""
Tic Tac t_oe Player
"""

import random

import numpy as np

X = 'X'
O = 'O'
EMPTY = None


def initial_stat_e():
    """
    Returns starting stat_e of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(user, board):
    """
    Returns player who has the next turn on a board.
    """
    cont_x = 0
    cont_o = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 'X':
                cont_x += 1
            if board[i][j] == 'O':
                cont_o += 1

    if cont_x == cont_o:
        return X
    if cont_x > cont_o:
        return O
    if cont_x < cont_o:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    list_actions = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                list_actions.append((i, j))

    return list_actions


def result(user, board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    board[i][j] = player(user, board)
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


def t_erminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    else:
        cont_emp = 0
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == X or board[i][j] == O:
                    cont_emp += 1
        if cont_emp == 9:
            return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    end = False
    ficha = ['X', 'O']
    value = [1, -1]
    cont = 0
    while cont < 2:
        cont_d1 = 0
        cont_d2 = 0
        cont_emp = 0
        for i in range(len(board)):
            cont_c = 0
            cont_f = 0
            for j in range(len(board)):
                if (i == j) and ((board[i][j]) == ficha[cont]):
                    cont_d1 += 1
                if (i + j) == 2 and (board[i][j]) == ficha[cont]:
                    cont_d2 += 1
                if board[i][j] == X or board[i][j] == O:
                    cont_emp += 1
                if board[i][j] == ficha[cont]:
                    cont_f += 1
                    if cont_f == 3:
                        end = value[cont]
                if board[j][i] == ficha[cont]:
                    cont_c += 1
                    if cont_c == 3:
                        end = value[cont]

        if cont_d1 == 3:
            end = value[cont]
        if cont_d2 == 3:
            end = value[cont]
        if cont_emp == 9 and not end:
            end = 0
        cont += 1
    if not end:
        end = 0

    return end


def minimax(user, board):
    """
    Returns the optimal action for the current player on the board.
    """
    optimal_action = []
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
                if winner(aux1) == player(user, aux):
                    pierde = True
                    break
                if not pierde:
                    for action2 in actions(aux1):
                        aux2 = np.copy(aux1)
                        aux2[action2[0]][action2[1]] = player(user, aux2)
                        if winner(aux2) == player(user, aux2):
                            pierde = True

        if not pierde:
            optimal_action.append(action)

    if len(optimal_action) > 0:
        return optimal_action[random.randint(0, len(optimal_action) - 1)]

    return actions(board)[random.randint(0, len(actions(board)) - 1)]
