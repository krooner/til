N = int(input())

l = []
for i in range(N):
    age, name = input().split()
    l.append((i, int(age), name))

l.sort(key=lambda x: (x[1], x[0]))
for _, age, name in l:
    print(age, name)