# SOLVED: https://www.acmicpc.net/problem/2529

from itertools import permutations

k = int(input())

inequals = input().split()

def check(numbers, inequals):
    answer = True
    lnum = numbers[0]
    for i in range(len(inequals)):
        symbol = inequals[i]
        rnum = numbers[i+1]

        if symbol == "<":
            if lnum >= rnum: return False
        else: # ">"
            if lnum <= rnum: return False

        lnum = rnum
    return answer

min_num = int("9" * (k+1))
max_num = -1

for nums in permutations([i for i in range(10)], len(inequals)+1):
    if check(list(nums), inequals):
        num_str = "".join(map(str, nums))
        num_int = int(num_str)

        min_num = min(min_num, num_int)
        max_num = max(max_num, num_int)

max_num_str = "0" * (k+1-len(str(max_num))) + str(max_num)
min_num_str = "0" * (k+1-len(str(min_num))) + str(min_num)

print(max_num_str)
print(min_num_str)