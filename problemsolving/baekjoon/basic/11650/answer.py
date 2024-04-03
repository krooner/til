N = int(input())

for x, y in sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: (x[0], x[1])):
    print(x, y)