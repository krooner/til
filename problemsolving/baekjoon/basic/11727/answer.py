N = int(input())

table = [0]*1001

table[1] = 1
table[2] = 3

for i in range(3, N+1):
    vertical = table[i-1]*1
    horizontal = table[i-2]*2
    table[i] = vertical + horizontal

print(table[N]%10007)
