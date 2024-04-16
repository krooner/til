import sys
input = sys.stdin.readline

N, M = map(int, input().split())

noheard = set()
common = []
for _ in range(N):
    noheard.add(input().strip())
for _ in range(M):
    item = input().strip()
    if item in noheard:
        common.append(item)

print(len(common))
for item in sorted(common):
    print(item)
