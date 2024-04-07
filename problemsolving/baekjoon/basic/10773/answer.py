K = int(input())

summation = []

for _ in range(K):
    number = int(input())
    if number == 0:
        summation.pop()
    else:
        summation.append(number)

print(sum(summation))
