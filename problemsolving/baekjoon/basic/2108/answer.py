from collections import Counter, defaultdict
import sys
input = sys.stdin.readline

N = int(input())
values = [int(input()) for _ in range(N)]

avg = int(round(sum(values)/len(values), 0))
med = sorted(values)[int(N/2)]

mode_dict = defaultdict(list)

max_cnt = 0
for v, cnt in Counter(values).most_common():
    mode_dict[cnt].append(v)
    max_cnt = max(max_cnt, cnt)

if len(mode_dict[max_cnt]) == 1:
    mode = mode_dict[max_cnt][0]
else:
    mode = sorted(mode_dict[max_cnt])[1]

range_ = max(values) - min(values)

print(avg)
print(med)
print(mode)
print(range_)
