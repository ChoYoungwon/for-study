def isSafe(board, x, y):
    N = len(board)

    for i in range(y):
        if board[i][x] == 1:
            return False
    for i, j in zip(range(y-1, -1, -1), range(x-1, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(y-1, -1, -1), range(x+1, N)):
        if board[i][j] == 1:
            return False
    return True

count = 0
def solve_N_Queen(board, y):
    N = len(board)
    if y == N:
        # printBoard(board)
        global count
        count += 1
        # print(count)
        return

    for x in range(N):
        if isSafe(board, x, y):
            board[y][x] = 1
            solve_N_Queen(board, y+1)
            board[y][x] = 0

def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


for i in range(4, 10):
    N = i
    board = [[0 for i in range(N)] for j in range(N)]
    solve_N_Queen(board, 0)
    print(f'{i}-Queen의 해의 개수 : ', count)
    count = 0

