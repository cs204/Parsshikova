"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


import copy

def player(board):
    # Возвращает, кто ходит следующим (X или O)
    return 'X' if board.count('X') <= board.count('O') else 'O'

def actions(board):
    # Возвращает set возможных действий (i, j) для пустых ячеек
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] is None}

def result(board, action):
    # Возвращает новое состояние доски после выполнения действия
    if board[action[0]][action[1]] is not None:
        raise Exception("Invalid action")
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board

def winner(board):
    # Возвращает победителя (X или O), если он есть
    winning_combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    for combination in winning_combinations:
        if board[combination[0][0]][combination[0][1]] == board[combination[1][0]][combination[1][1]] == board[combination[2][0]][combination[2][1]] != None:
            return board[combination[0][0]][combination[0][1]]
    return None

def terminal(board):
    # Возвращает True, если игра закончена
    return winner(board) is not None or all(cell is not None for row in board for cell in row)

def utility(board):
    # Возвращает -1, 0, 1 для терминального состояния доски
    if winner(board) == 'O':
        return -1
    elif winner(board) == 'X':
        return 1
    else:
        return 0

def minimax(board):
    # Возвращает оптимальный ход для текущего игрока
    if terminal(board):
        return None

    def max_value(board):
        if terminal(board):
            return utility(board)
        v = float('-inf')
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

    def min_value(board):
        if terminal(board):
            return utility(board)
        v = float('inf')
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v

    current_player = player(board)
    if current_player == 'X':
        best_val = float('-inf')
        best_move = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_val:
                best_val = value
                best_move = action
    else:
        best_val = float('inf')
        best_move = None
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_val:
                best_val = value
                best_move = action
    return best_move
