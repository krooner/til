from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())

for _ in range(T):
    M, N, K = list(map(int, input().split()))

    board = [[0]*M for _ in range(N)]
    locs = [list(map(int, input().split())) for _ in range(K)]
    visited = [[False]*M for _ in range(N)]

    for c, r in locs:
        board[r][c] = 1

    def solve(r, c):
        dq = deque([(r, c)])

        while len(dq) != 0:
            for _ in range(len(dq)):
                r, c = dq.popleft()

                for i in range(4):
                    rr, cc = r+dr[i], c+dc[i]
                    if 0<=rr<N and 0<=cc<M and \
                            board[rr][cc] == 1 and visited[rr][cc]==False:
                        visited[rr][cc] = True
                        dq.append((rr, cc))
        
        return
    
    cnt = 0

    for r in range(N):
        for c in range(M):
            if board[r][c] == 1 and visited[r][c] == False:
                cnt += 1
                visited[r][c] = True
                solve(r, c)

    print(cnt)
