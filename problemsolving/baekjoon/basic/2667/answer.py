from collections import deque, defaultdict

N = int(input())
board = [list(map(int, list(input()))) for _ in range(N)]
paint = [[False]*N for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def solve(ir, ic):
    answer = 0
    dq = deque([(ir, ic)])
    paint[ir][ic]=True

    while len(dq) != 0:
        for _ in range(len(dq)):
            r, c = dq.popleft()
            answer += 1

            for i in range(4):
                rr, cc = r+dr[i], c+dc[i]
                if 0<=rr<N and 0<=cc<N and board[rr][cc]==1 and paint[rr][cc]==False:
                    paint[rr][cc] = True
                    dq.append((rr, cc))
    return answer

l = []

for r in range(N):
    for c in range(N):
        if board[r][c] == 1 and paint[r][c] == False:
            l.append(solve(r, c))

print(len(l))
for item in sorted(l):
    print(item)