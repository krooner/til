from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
elapse = [100001] * 200001

min_time = 100001

dq = deque([(N, 0)])
elapse[N] = 0

while len(dq) != 0:
    for _ in range(len(dq)):
        node, t = dq.popleft()
        if node == K:
            min_time = min(min_time, t)
        if 0<=node-1<len(elapse) and t+1 < elapse[node-1]:
            elapse[node-1] = t+1
            dq.append((node-1, t+1))
        if 0<=node+1<len(elapse) and t+1 < elapse[node+1]: 
            elapse[node+1] = t+1
            dq.append((node+1, t+1))
        if 0<=node*2<len(elapse) and t+1 < elapse[node*2]:
            elapse[node*2] = t+1
            dq.append((node*2, t+1))

print(min_time)