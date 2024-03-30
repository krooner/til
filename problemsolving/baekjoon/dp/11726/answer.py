n = int(input())

dp_table = [0] * 1001

dp_table[1] = 1
dp_table[2] = 2

for i in range(3, 1001):
    dp_table[i] = (dp_table[i-1]+dp_table[i-2])%10007

print(dp_table[n])