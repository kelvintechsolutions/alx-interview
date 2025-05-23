#!/usr/bin/python3
import sys

def validate_args():
    '''
    Validates the command-line arguments
    '''
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    return N

def is_safe(board, row, col):
    '''
    Checks safe places for queen
    '''
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N):
    '''
    Solves the N Queens problem using backtracking
    '''
    def backtrack(row, board):
        if row == N:
            result.append(board[:])
            return
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1, board)
                board[row] = -1

    result = []
    board = [-1] * N
    backtrack(0, board)
    return result

def print_solutions(solutions):
    '''
    Outputs all solutions in the required format.
    '''
    for solution in solutions:
        formatted_solution = [[i, solution[i]] for i in range(len(solution))]
        print(formatted_solution)

if __name__ == "__main__":
    N = validate_args()
    solutions = solve_nqueens(N)
    print_solutions(solutions)

