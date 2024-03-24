from itertools import permutations

N, S = list(map(int, input().split()))
numbers = list(map(int, input().split()))

items = []
answer = 0

def dfs(idx):
    global answer
    if idx == len(numbers):
        if len(items) == 0: return
        if sum(items) == S:
            answer += 1
        return
    
    items.append(numbers[idx])
    dfs(idx+1)
    items.pop()
    dfs(idx+1)

dfs(0)

print(answer)