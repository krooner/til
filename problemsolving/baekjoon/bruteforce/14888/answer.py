# SOLVED: https://www.acmicpc.net/problem/14888

from itertools import permutations

N = int(input())
A = list(map(int, input().split()))

# 0 1 2 3
# + - * /
symbol_cnts = list(map(int, input().split()))

symbols = []
for i in range(len(symbol_cnts)):
    symbols += [i] * symbol_cnts[i]

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

for ordered_syms in permutations(symbols, len(symbols)):
    result = calculate(list(ordered_syms))
    min_val = min(result, min_val)
    max_val = max(result, max_val)

print(max_val)
print(min_val)
