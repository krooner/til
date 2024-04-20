import sys
stdin = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def find(r, c):
    global num_person
    dq = deque([(r, c)])

    while len(dq) != 0:
        for _ in range(len(dq)):
            rr, cc = dq.popleft()

            for i in range(4):
                nr, nc = rr+dr[i], cc+dc[i]

                if 0<=nr<N and 0<=nc<M and board[nr][nc] not in ["I", "X"] and visited[nr][nc] == False:
                    if board[nr][nc] == "P":
                        num_person += 1
                    visited[nr][nc] = True
                    dq.append((nr, nc))

num_person = 0
for r in range(N):
    for c in range(M):
        if board[r][c] == 'I':
            find(r, c)
            break

if num_person == 0:
    print("TT")
else:
    print(num_person)