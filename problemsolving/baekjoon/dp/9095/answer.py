T = int(input())

dp_table = [0] * 12

dp_table[1] = 1 # 1
dp_table[2] = 2 # 1+f(1), f(2)
dp_table[3] = 4 # 1+1+1, 1+2, 2+1, 3

for i in range(4, 12):
    dp_table[i] = dp_table[i-1]+dp_table[i-2]+dp_table[i-3]

for _ in range(T):
    n = int(input())

    print(dp_table[n])