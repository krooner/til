import sys
input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
length = N

white = blue = 0

while length >= 1:
    for r in range(0, N, length):
        for c in range(0, N, length):
            
            if visited[r][c]:
                continue

            criterion = None
            for i in range(length*length):
                cr = r + i//length
                cc = c + i%length
                if criterion == None:
                    criterion = board[cr][cc]
                else:
                    if board[cr][cc] != criterion:
                        criterion = -1
                        break
            
            if criterion != -1:
                if criterion == 0:
                    white += 1
                else:
                    blue += 1
                for i in range(length*length):
                    cr = r + i//length
                    cc = c + i%length
                    visited[cr][cc] = True
                    
    length = int(length/2)
print(white)
print(blue)