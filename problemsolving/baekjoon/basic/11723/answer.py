import sys
input = sys.stdin.readline

M = int(input())

S = set()
for _ in range(M):
    
    l = input().split()
    if l[0] == 'add':
        value = int(l[1])
        if value not in S:
            S.add(value)
    elif l[0] == 'remove':
        value = int(l[1])
        if value in S:
            S.remove(value)
    elif l[0] == 'check':
        value = int(l[1])
        print(1 if value in S else 0)
    elif l[0] == 'toggle':
        value = int(l[1])
        if value in S:
            S.remove(value)
        else:
            S.add(value)
    elif l[0] == 'all':
        S = set(list(range(1, 21)))
    elif l[0] == 'empty':
        S = set()