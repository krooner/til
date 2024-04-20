from collections import defaultdict
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    clothes = defaultdict(list)

    for _ in range(N):
        name, kind = input().split()
        clothes[kind].append(name)
    
    answer = 1
    for k, v in clothes.items():
        answer *= len(v)+1
    answer -= 1

    print(answer)