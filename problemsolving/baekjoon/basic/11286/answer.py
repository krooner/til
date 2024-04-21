import sys
import heapq
input = sys.stdin.readline

N = int(input())

l = []
heapq.heapify(l)

for _ in range(N):
    num = int(input())
    if num != 0:
        heapq.heappush(l, (abs(num), num))
    else:
        if len(l) == 0:
            print(0)
        else:
            item = heapq.heappop(l)
            heapq.heappush(l, item)
            mins = []
            while len(l) != 0:
                ele = heapq.heappop(l)
                if ele[0] != item[0]:
                    heapq.heappush(l, ele)
                    break
                else:
                    mins.append(ele)
            mins.sort(key=lambda x: x[1])
            for i in range(1, len(mins)):
                heapq.heappush(l, mins[i])
            print(mins[0][1])