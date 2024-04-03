from collections import deque
N = int(input())

dq = deque([i for i in range(1, N+1)])

while len(dq) > 1:
    _ = dq.popleft()
    e = dq.popleft()
    dq.append(e)

print(dq[0])