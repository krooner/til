# SOLVED: https://www.acmicpc.net/problem/14889

from itertools import combinations, permutations

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

min_diff = 1e10

def calculate(input_list):
    answer = 0
    for pick in permutations(input_list, 2):
        answer += board[pick[0]][pick[1]]
    return answer

for comb in combinations([i for i in range(N)], N//2):
    start = list(comb)
    link = [i for i in range(N) if i not in start]

    min_diff = min(min_diff, abs(calculate(start)-calculate(link)))

print(min_diff)