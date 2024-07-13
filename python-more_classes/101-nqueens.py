#!/usr/bin/python3
import sys

def nqueens(N):
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N  # Initialize the board with -1 indicating no queen

    def is_safe(row, col):
        for prev_row in range(row):
            prev_col = board[prev_row]
            if prev_col == col or abs(prev_col - col) == row - prev_row:
                return False
        return True

    def print_solution():
        solution = []
        for row in range(N):
            line = ['.' for _ in range(N)]
            line[board[row]] = 'Q'
            solution.append("".join(line))
        print("\n".join(solution))
        print()

    def solve(row):
        if row == N:
            print_solution()
            return
        for col in range(N):
            if is_safe(row, col):
                board[row] = col
                solve(row + 1)
                board[row] = -1

    solve(0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(N)

