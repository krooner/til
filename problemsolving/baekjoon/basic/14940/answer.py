from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

goal = None

for r in range(n):
    for c in range(m):
        if board[r][c] == 2:
            goal = (r, c, 0)

dq = deque([goal])
visited[goal[0]][goal[1]] = goal[2]

while len(dq) != 0:
    for _ in range(len(dq)):
        r, c, dist = dq.popleft()

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            if 0<=rr<n and 0<=cc<m and visited[rr][cc] == -1 and board[rr][cc] != 0:
                visited[rr][cc] = dist+1
                dq.append((rr, cc, dist+1))

for r in range(n):
    for c in range(m):
        if board[r][c] == 0:
            print(0, end=" ")
        else:
            print(visited[r][c], end=" ")
    print()