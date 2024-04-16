eq = input()

answer = 0
for i, item in enumerate(eq.split("-")):
    chunks = sum(list(map(int, item.split("+"))))
    if i == 0:
        answer += chunks
    else:
        answer -= chunks

print(answer)
