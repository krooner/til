N = int(input())

start = 1
answer = 0
for num in range(1, N+1):
    start *= num
    while True:
        q, r = divmod(start, 10)
        if r != 0:
            break
        else:
            answer += 1
            start = q

print(answer)
