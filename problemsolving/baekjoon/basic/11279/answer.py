import sys
input = sys.stdin.readline
import heapq
N = int(input())

l = []
heapq.heapify(l)

for _ in range(N):
    num = int(input())

    if num == 0:
        if len(l) == 0:
            print(0)
        else:
            min_val = heapq.heappop(l)
            print(-1*min_val)
    else:
        heapq.heappush(l, -1*num)