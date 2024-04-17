import sys
input = sys.stdin.readline

N, M = map(int, input().split())

num_name = dict()
name_num = dict()

for i in range(N):
    num = i+1
    name = input().strip()
    num_name[num] = name
    name_num[name] = num

for _ in range(M):
    input_str = input().strip()
    if input_str.isnumeric():
        print(num_name[int(input_str)])
    else:
        print(name_num[input_str])
