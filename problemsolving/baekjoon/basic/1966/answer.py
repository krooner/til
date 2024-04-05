from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    # p, odr
    priorities = zip(map(int, input().split()), [i for i in range(N)])

    print_order = []

    dq = deque(priorities)

    while len(dq) != 0:
        ele = dq.popleft()
        max_val = max([item[0] for item in dq]) if len(dq) != 0 else 0
        if ele[0] >= max_val:
            print_order.append(ele[1]) 
        else:
            dq.append(ele)
    
    print(print_order.index(M)+1)
