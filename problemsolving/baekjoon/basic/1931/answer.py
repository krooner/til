N = int(input())

times = [tuple(map(int, input().split())) for _ in range(N)]
times.sort(key=lambda x: (x[1], x[0]))

cnt = 0
prev = 0
for s, e in times:
    if s >= prev:
        cnt += 1
        prev = e

print(cnt)