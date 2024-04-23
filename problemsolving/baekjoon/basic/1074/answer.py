from collections import deque
import sys
input = sys.stdin.readline

N, R, C = map(int, input().split())

answer = 0
dr = [0, 0, 1, 1]
dc = [0, 1, 0, 1]
"""
0 1
2 3
"""

biscuit = []
gogo = N
sp = (0, 0)
while gogo >= 1:
    interval = pow(2, gogo-1)
    for i in range(4):
        crit_r, crit_c = sp[0] + interval*dr[i], sp[1] + interval*dc[i]
        if crit_r<=R<crit_r+interval and crit_c<=C<crit_c+interval:
            sp = (crit_r, crit_c)
            biscuit.append(i)
    gogo -= 1

for i, idx in enumerate(biscuit):
    answer += (pow(2, N-i-1)**2)*idx

print(answer) 