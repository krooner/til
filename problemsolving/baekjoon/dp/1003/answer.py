T = int(input())

dp_table = [[None, None] for _ in range(41)]
dp_table[0] = [1, 0]
dp_table[1] = [0, 1]
dp_table[2] = [1, 1]

for i in range(3, 41):
    dp_table[i] = [dp_table[i-1][0]+dp_table[i-2][0], dp_table[i-1][1]+dp_table[i-2][1]]

for _ in range(T):
    N = int(input())

    print(dp_table[N][0], dp_table[N][1])