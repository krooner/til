from collections import defaultdict, deque

N = int(input())
P = int(input())

pairs = [tuple(map(int, input().split())) for _ in range(P)]

graph = defaultdict(list)

for src, dst in pairs:
    graph[src].append(dst)
    graph[dst].append(src)

visited = [False]*(N+1)

dq = deque([1])
cnt = 0
while len(dq) != 0:
    for _ in range(len(dq)):
        node = dq.popleft()
        if not visited[node]:
            visited[node] = True
            cnt += 1
        
            leaves = graph[node]
            for leaf in leaves:
                dq.append(leaf)

print(cnt-1)