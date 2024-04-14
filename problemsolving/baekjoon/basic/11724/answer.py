import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(M)]

visited = [False]*(N+1)

graph = [[] for _ in range(N+1)]
for u, v in points:
    graph[u].append(v)
    graph[v].append(u)

def dfs(node):
    visited[node] = True
    for leaf in graph[node]:
        if not visited[leaf]:
            dfs(leaf)

cnt = 0
for inode in range(1, N+1):
    if not visited[inode]:
        dfs(inode)
        cnt += 1

print(cnt)