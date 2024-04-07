N = int(input())

values = [tuple(map(int, input().split())) for _ in range(N)]
values.sort(key=lambda x: (x[1], x[0]))

for x, y in values:
    print(x, y)
