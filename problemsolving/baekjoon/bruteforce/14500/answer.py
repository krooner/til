# u, r, d, l
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = list(map(int, input().split()))

visited = [[False for _ in range(M)] for _ in range(N)]
board = [list(map(int, input().split())) for _ in range(N)]

answer = 0

def move(r, c, acc, cnt):
    global answer
    if cnt == 4:
        answer = max(acc, answer)
        return
    if r < 0 or r >= N or c < 0 or c >= M: return
    if visited[r][c]: return

    visited[r][c] = True
    for i in range(4):
        move(r+dr[i], c+dc[i], acc+board[r][c], cnt+1)
    visited[r][c] = False

for r in range(N):
    for c in range(M):
        move(r, c, 0, 0)
        if 0<=r<N and 0<=c<M and 0<=r+dr[0]<N and 0<=c+dc[0]<M and 0<=r+dr[1]<N and 0<=c+dc[1]<M and 0<=r+dr[2]<N and 0<=c+dc[2]<M: # ㅏ
             answer = max(answer, board[r][c]+board[r+dr[0]][c+dc[0]]+board[r+dr[1]][c+dc[1]]+board[r+dr[2]][c+dc[2]])

        if 0<=r<N and 0<=c<M and 0<=r+dr[0]<N and 0<=c+dc[0]<M and 0<=r+dr[3]<N and 0<=c+dc[3]<M and 0<=r+dr[2]<N and 0<=c+dc[2]<M: # ㅓ
             answer = max(answer, board[r][c]+board[r+dr[0]][c+dc[0]]+board[r+dr[3]][c+dc[3]]+board[r+dr[2]][c+dc[2]])

        if 0<=r<N and 0<=c<M and 0<=r+dr[3]<N and 0<=c+dc[3]<M and 0<=r+dr[0]<N and 0<=c+dc[0]<M and 0<=r+dr[1]<N and 0<=c+dc[1]<M: # ㅗ
             answer = max(answer, board[r][c]+board[r+dr[3]][c+dc[3]]+board[r+dr[0]][c+dc[0]]+board[r+dr[1]][c+dc[1]])

        if 0<=r<N and 0<=c<M and 0<=r+dr[3]<N and 0<=c+dc[3]<M and 0<=r+dr[2]<N and 0<=c+dc[2]<M and 0<=r+dr[1]<N and 0<=c+dc[1]<M: # ㅜ
             answer = max(answer, board[r][c]+board[r+dr[3]][c+dc[3]]+board[r+dr[2]][c+dc[2]]+board[r+dr[1]][c+dc[1]])

print(answer)