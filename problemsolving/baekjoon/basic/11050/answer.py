N, K = map(int, input().split())

numerator = 1
for i in range(1, N+1):
    numerator *= i

denom = 1
for i in range(1, K+1):
    denom *= i
for i in range(1, (N-K)+1):
    denom *= i

print(numerator//denom)