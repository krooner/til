T = int(input())

board = [[i for i in range(15)] for _ in range(15)]

for a in range(1, 15):
    for b in range(1, 15):
        board[a][b] = sum([board[a-1][i] for i in range(1, b+1)])

for _ in range(T):
    k = int(input())
    n = int(input())

    print(board[k][n])