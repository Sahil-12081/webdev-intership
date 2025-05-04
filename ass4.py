def printSolution(board, N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

def isSafe(board, row, col, N):
    # Check this row on the left
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQUtil(board, col, N, solution_found):
    # Base case: All queens placed
    if col >= N:
        print("One of the possible solutions is:")
        printSolution(board, N)
        solution_found[0] = True  # Bound condition to stop
        return True

    for i in range(N):
        if isSafe(board, i, col, N):
            board[i][col] = 1
            if solveNQUtil(board, col + 1, N, solution_found):
                return True
            board[i][col] = 0  # Backtrack

        if solution_found[0]:
            break  # Bound: prune remaining branches

    return False

def solveNQ(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    solution_found = [False]  # Mutable flag for bounding

    if not solveNQUtil(board, 0, N, solution_found):
        print("Solution does not exist")

# Example: Solve for any N
N = int(input("Enter the value of N: "))
solveNQ(N)
