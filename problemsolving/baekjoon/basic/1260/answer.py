from collections import defaultdict
from collections import deque

N, M, V = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for key in graph.keys():
    graph[key].sort()

# dfs
order_dfs = [V]
visited = [False] * 1001
visited[V] = True

def dfs(node):
    # if not visited[node]:
    #     order_dfs.append(node)
    #     visited[node] = True
    
    next_nodes = graph[node]
    for nnode in next_nodes:
        # dfs(nnode)
        if not visited[nnode]:
            order_dfs.append(nnode)
            visited[nnode] = True
            dfs(nnode)

dfs(V)
print(" ".join(map(str, order_dfs)))


# bfs
dq = deque([V])
visited = [False] * 1001
order_bfs = []

while len(dq) != 0:
    for _ in range(len(dq)):
        snode = dq.popleft()
        if not visited[snode]:
            visited[snode] = True
            order_bfs.append(snode)
            for nnode in graph[snode]:
                dq.append(nnode)

print(" ".join(map(str, order_bfs)))
