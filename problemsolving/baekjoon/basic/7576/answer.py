M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

num_tomato = 0
for r in range(N):
    for c in range(M):
        if board[r][c] != -1:
            num_tomato += 1

day = 0

ripes = []
for r in range(N):
    for c in range(M):
        if board[r][c] == 1:
            ripes.append((r, c))
acc_ripes = len(ripes)

while True:
    num_update = 0
    new_ripes = set()

    for r, c in ripes:
        for i in range(4):
            rr = r+dr[i]
            cc = c+dc[i]

            if 0<=rr<N and 0<=cc<M and board[rr][cc] == 0:
                num_update += 1
                board[rr][cc] = 1
                new_ripes.add((rr, cc))

    acc_ripes += len(new_ripes)
    ripes = new_ripes

    if num_update == 0:
        if num_tomato != acc_ripes:
            print(-1)
            break
        else:
            print(day)
            break
    day += 1