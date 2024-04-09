from collections import deque

N, M = map(int, input().split())

board = [list(map(int, list(input()))) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

dq = deque([(0, 0, 1)])

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

answer = 0

while len(dq) != 0:
    for _ in range(len(dq)):
        r, c, cnt = dq.popleft()

        if r==N-1 and c==M-1:
            answer = cnt
            continue

        for i in range(4):
            rr = r+dr[i]
            cc = c+dc[i]

            if 0<=rr<N and 0<=cc<M and board[rr][cc] != 0:
                if not visited[rr][cc]:
                    dq.append((rr, cc, cnt+1))
                    visited[rr][cc] = True

print(answer)