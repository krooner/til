from itertools import combinations, permutations

N = int(input())
A = list(map(int, input().split()))

# 0 1 2 3
# + - * /
symbol_cnts = list(map(int, input().split()))

min_val = 1e10
max_val = -1e10

def calculate(input_syms):
    lvalue = A[0]
    for i in range(1, len(A)):
        rvalue = A[i]
        symbol = input_syms[i-1]
        if symbol == 0:
            lvalue += rvalue
        elif symbol == 1:
            lvalue -= rvalue
        elif symbol == 2:
            lvalue *= rvalue
        else:
            if lvalue < 0:
                q, r = divmod(-1*lvalue, rvalue)
                lvalue = -q
            else:
                lvalue = lvalue // rvalue
    return lvalue

items = []

def dfs(depth):
    global min_val, max_val
    if depth == len(A)-1:
        result = calculate(items)
        min_val = min(result, min_val)
        max_val = max(result, max_val)
        return
    
    for i in range(len(symbol_cnts)):
        spare = symbol_cnts[i]
        if spare > 0:
            items.append(i)
            symbol_cnts[i] -= 1
            dfs(depth+1)
            symbol_cnts[i] += 1
            items.pop()

    return

dfs(0)

print(max_val)
print(min_val)