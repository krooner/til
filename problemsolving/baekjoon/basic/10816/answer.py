from collections import Counter

N = int(input())

l = map(int, input().split())
cnt_dict = dict(Counter(l))

M = int(input())
for num in map(int, input().split()):
    if num not in cnt_dict:
        print(0, end=" ")
    else:
        print(cnt_dict[num], end=" ")