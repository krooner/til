N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

# use
# no-use
min_cnt = 1e8

def dfs(idx, left, count):
    global min_cnt
    if idx == -1:
        if left == 0:
            min_cnt = min(min_cnt, count)
        return

    q, r = divmod(left, coins[idx])

    dfs(idx-1, r, count+q) # use
    dfs(idx-1, left, count) # no use

dfs(N-1, K, 0)

print(min_cnt)