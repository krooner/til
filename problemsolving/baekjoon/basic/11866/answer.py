N, K = map(int, input().split())

circle = [i for i in range(1, N+1)]

l = []

idx = K-1
while len(circle) != 0:
    idx %= len(circle)
    item = circle[idx]

    l.append(item)
    temp = circle.copy()
    circle = temp[:idx] + temp[idx+1:]

    idx += K-1

string = list(str(l))
string[0] = "<"
string[-1] = ">"
print("".join(string))