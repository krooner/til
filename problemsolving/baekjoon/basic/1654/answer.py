K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]
answer = 0

minl = 1
maxl = max(lines)

while minl <= maxl:
    mid = int((minl+maxl)/2)

    cnt = 0
    for line in lines:
        cnt += line//mid
    
    if cnt >= N:
        if answer < mid:
            answer = mid
        minl = mid+1
    else:
        maxl = mid-1

print(answer)