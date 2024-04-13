import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

min_val = min([min(board[i]) for i in range(N)])
max_val = max([max(board[i]) for i in range(N)])

def height_time(h):
    hB = B
    h_time = 0
    for r in range(N):
        for c in range(M):
            value = board[r][c]
            if value < h:
                hB -= (h - value)
                h_time += (h-value) * 1
            else: # value >= floor
                hB += (value - h)
                h_time += (value-h) * 2
    if hB < 0:
        return -1
    else:
        return h_time

min_time = 1e9
min_height = None
for h in range(min_val, max_val+1):
    htime = height_time(h)
    if htime == -1: continue
    if htime < min_time:
        min_time = htime
        min_height = h
    elif htime == min_time:
        min_height = max(min_height, h)

print(min_time, min_height)