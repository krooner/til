
# u, r, d, l
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

figures = [
    ["R", "RR", "RRR"], ["D", "DD", "DDD"], ["U", "UU", "UUU"], ["L", "LL", "LLL"], # -
    ["R", "RD", "D"], # ㅁ
    ["L", "R", "D"], ["D", "U", "L"], ["L", "R", "U"], ["U", "D", "R"], # ㅗ
    ["U", "R", "RD"], ["U", "L", "LD"], ["L", "U", "UR"], ["R", "U", "UL"], # z
    ["U", "R", "RR"], ["U", "L", "LL"], ["D", "R", "RR"], ["D", "L", "LL"], ["L", "D", "DD"], ["R", "D", "DD"], ["L", "U", "UU"], ["R", "U", "UU"] # ㄴ
]

N, M = list(map(int, input().split()))

visited = [[False for _ in range(M)] for _ in range(N)]
board = [list(map(int, input().split())) for _ in range(N)]

answer = -1

def check(r, c, input_fig):
    if visited[r][c]: 
        return False
    for string in input_fig:
        init_r, init_c = r, c
        for char in list(string):
            if char == "U":
                init_r += dr[0]
                init_c += dc[0]
            elif char == "R":
                init_r += dr[1]
                init_c += dc[1]
            elif char == "D":
                init_r += dr[2]
                init_c += dc[2]
            else: # L
                init_r += dr[3]
                init_c += dc[3]
        if 0<=init_r<N and 0<=init_c<M and (not visited[init_r][init_c]):
            pass
        else:
            return False
    return True

def apply(r, c, input_fig, value):
    visited[r][c] = value
    for string in input_fig:
        init_r, init_c = r, c
        for char in list(string):
            if char == "U":
                init_r += dr[0]
                init_c += dc[0]
            elif char == "R":
                init_r += dr[1]
                init_c += dc[1]
            elif char == "D":
                init_r += dr[2]
                init_c += dc[2]
            else: # L
                init_r += dr[3]
                init_c += dc[3]
        visited[init_r][init_c] = value
    return

def calculate():
    accum = 0
    for r in range(N):
        for c in range(M):
            if visited[r][c]: accum += board[r][c]
    return accum

def dfs(r, c):
    global answer
    if r == N:
        answer = max(answer, calculate())
        return

    for rr in range(r, N):
        for cc in range(c, M):

            for figure in figures:
                if check(rr, cc, figure):
                    apply(rr, cc, figure, True)
                    next_r, next_c = rr, cc
                    if cc == M-1:
                        next_r += 1
                        next_c = 0
                    else:
                        next_c += 1
                    dfs(next_r, next_c)
                    apply(rr, cc, figure, False)


dfs(0, 0)

print(answer)