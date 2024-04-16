# pypy3

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

answer = 0
def binary_search(l, r):
    global answer
    if l > r:
        return

    mid = int((l+r)/2)
    value = sum([max(item-mid, 0) for item in trees])

    if value < M:
        binary_search(l, mid-1)
    if value >= M:
        answer = max(answer, mid)
        binary_search(mid+1, r)

    return

binary_search(1, max(trees))
print(answer)
