#!/usr/bin/python3
import sys

def is_safe(cols, row, col):
    """Check if placing a queen at (row, col) is safe."""
    for i in range(row):
        if cols[i] == col or abs(i - row) == abs(cols[i] - col):
            return False
    return True

def backtrack(n, row, cols, solutions):
    """Recursively find all valid N-Queens solutions."""
    if row == n:
        solutions.append([[i, cols[i]] for i in range(n)])
        return
    for col in range(n):
        if is_safe(cols, row, col):
            cols.append(col)
            backtrack(n, row + 1, cols, solutions)
            cols.pop()

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = []
    backtrack(n, 0, [], solutions)
    for sol in solutions:
        print(sol)

if __name__ == "__main__":
    main()

