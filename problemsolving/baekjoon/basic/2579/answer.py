N = int(input())
points = [int(input()) for _ in range(N)]

scores = [[0, 0] for _ in range(N+1)]
for i in range(len(points)):
    idx = i+1
    scores[idx][0] = max(scores[max(0, idx-2)]) + points[i]
    scores[idx][1] = scores[max(0, idx-1)][0] + points[i]

print(max(scores[N]))