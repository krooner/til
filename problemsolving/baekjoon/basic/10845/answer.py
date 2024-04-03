from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

queue = deque([])

for _ in range(N):
    commands = input().split()
    if len(commands) == 1:
        cmd = commands[0]
        if cmd == 'front':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[0])
        elif cmd == 'back':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[-1])
        elif cmd == 'size':
            print(len(queue))
        elif cmd == 'empty':
            print(0 if len(queue) != 0 else 1)
        elif cmd == 'pop':
            if len(queue) == 0:
                print(-1)
            else:
                e = queue.popleft()
                print(e)
        else:
            raise ValueError()
    else:
        queue.append(int(commands[1]))