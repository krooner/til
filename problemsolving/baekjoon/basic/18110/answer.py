import sys
input = sys.stdin.readline

n = int(input())
values = sorted([int(input()) for _ in range(n)])

def round_custom(x):
    if x - int(x) >= 0.5:
        return int(x)+1
    else:
        return int(x)

offset = round_custom(.15*n)

numerator = sum(values[offset:n-offset])
denominator = n - (2*offset)

print(round_custom(numerator/denominator) if n != 0 else 0)
