import sys
input = sys.stdin.readline

N, M = map(int, input().split())
acc = [0]*(N+1) 
for i, value in enumerate(list(map(int, input().split()))):
    acc[i+1] = value + acc[i]

for _ in range(M):
    a, b = map(int, input().split())
    print(acc[b]-acc[a-1])