# N = int(input("Enter no of queens: "))

# # for printing boards
# board = [[0]*N for _ in range(N)]


# def attack(i, j):

#     for k in range(0, N):
#         if board[i][k] == 1 or board[k][j] == 1:
#             return True

#     for k in range(0, N):
#         for l in range(0, N):
#             if (k+l == i+j) or (k-l == i-j):

#                 if board[k][l] == 1:
#                     return True
#     return False


# def N_queens(n):
#     if n == 0:
#         return True
#     for i in range(0, N):
#         for j in range(0, N):
#             if (not (attack(i, j))) and (board[i][j] != 1):
#                 board[i][j] = 1
#                 if N_queens(n-1) == True:
#                     return True
#                 board[i][j] = 0
#     return False


# N_queens(N)
# for i in board:
#     print(i)


def is_safe(board, row, col, N):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check if there is a queen in the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # The position is safe
    return True


def solve_n_queens(board, col, N):
    # Base case: all queens have been placed
    if col == N:
        return True

    # Try placing the queen in each row of the current column
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place the queen in the current position
            board[i][col] = 1

            # Recursively place the remaining queens
            if solve_n_queens(board, col + 1, N):
                return True

            # Backtrack: remove the queen from the current position
            board[i][col] = 0

    # Could not find a safe position for the queen in the current column
    return False


def print_board(board):
    N = len(board)
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

# Driver code
N = int(input("Enter the number of queens: "))
board = [[0 for i in range(N)] for j in range(N)]

if solve_n_queens(board, 0, N):
    print_board(board)
else:
    print("Solution does not exist")

