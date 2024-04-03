from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

dq = deque([])

for _ in range(N):
    cmds = input().split()

    if cmds[0] == 'push_front':
        dq.appendleft(cmds[1])
    elif cmds[0] == 'push_back':
        dq.append(cmds[1])
    elif cmds[0] == 'pop_front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif cmds[0] == 'pop_back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())
    elif cmds[0] == 'size':
        print(len(dq))
    elif cmds[0] == 'empty':
        print(0 if len(dq) != 0 else 1)
    elif cmds[0] == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif cmds[0] == 'back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
    else:
        raise ValueError()