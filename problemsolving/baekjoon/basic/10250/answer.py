T = int(input())

for _ in range(T):
    H, W, N = list(map(int, input().split()))

    q, r = divmod(N, H)

    if r == 0:
        prefix = str(H)
        suffix = '0'+str(q) if len(str(q)) == 1 else str(q)

    else:
        prefix = str(r)
        suffix = '0'+str(q+1) if len(str(q+1)) == 1 else str(q+1)

    print(f"{prefix}{suffix}")