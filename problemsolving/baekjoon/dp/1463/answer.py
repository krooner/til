N = int(input())

dp_table = [50] * 1000001

dp_table[1] = 0
dp_table[2] = 1
dp_table[3] = 1
dp_table[4] = 2

for X in range(1, N+1):
    if X%3 == 0: # 3
        dp_table[X] = min(dp_table[X], 1+dp_table[X//3])
        if X%2 == 0: # 6
            dp_table[X] = min(dp_table[X], 1+dp_table[X//2])
    else: 
        # X%3 != 0
        if X%2 == 0:
            dp_table[X] = min(dp_table[X], 1+dp_table[X//2])
    dp_table[X] = min(dp_table[X], 1+dp_table[X-1])

print(dp_table[N])