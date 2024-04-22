import sys
input = sys.stdin.readline

N = int(input())

values = list(map(int, input().split()))
sortvs = sorted(set(values))

def search(l, r, v):
    if l > r:
        return -1
    
    mid = int((l+r)/2)
    if sortvs[mid] == v:
        return mid
    elif sortvs[mid] > v:
        return search(l, mid-1, v)
    else:
        return search(mid+1, r, v)

for v in values:
    print(search(0, len(sortvs)-1, v), end=" ")