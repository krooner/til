import sys
input = sys.stdin.readline

import math
N = int(input())

table = [5]*50001
table[1] = 1

for v in range(1, N+1):
    vrt = int(math.sqrt(v))
    if v//vrt == vrt and v%vrt == 0:
        table[v] = 1
    else:
        for dec in range(vrt, 0, -1):
            r = v-dec**2
            table[v] = min(table[v], 1+table[r])

print(table[N])