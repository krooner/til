N = int(input())
S = list(map(int, input().split()))

flags = [0] * (100000 * 20 + 1)

items = []

def dfs(idx):
    global min_val
    if idx == len(S):
        if len(items) == 0: return
        flags[sum(items)] = 1
        return
    
    items.append(S[idx])
    dfs(idx+1)
    items.pop()
    dfs(idx+1)

dfs(0)

idx = 1
while True:
    if flags[idx] == 0:
        break
    idx += 1

print(idx)