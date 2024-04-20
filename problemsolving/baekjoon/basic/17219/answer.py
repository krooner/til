import sys
input = sys.stdin.readline

N, M = map(int, input().split())

updic = dict()

for _ in range(N):
    url, pw = input().split()
    updic[url] = pw
for _ in range(M):
    url = input().strip()
    print(updic[url])