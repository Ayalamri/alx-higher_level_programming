#!/usr/bin/python3
"""
N queens puzzle solution
"""

import sys

def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen in a specific position
    """
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve(board, row, n):
    """
    Recursive function to solve N Queens problem
    """
    if row == n:
        print([[i, board[i]] for i in range(n)])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve(board, row + 1, n)

def nqueens(n):
    """
    Solve N Queens problem and print solutions
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [-1] * n
    solve(board, 0, n)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    nqueens(n)
