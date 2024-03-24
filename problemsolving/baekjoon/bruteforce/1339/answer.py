# SOLVED: https://www.acmicpc.net/problem/1339

from collections import defaultdict

N = int(input())

max_length = -1
words = []
for _ in range(N):
    word = input()
    max_length = max(max_length, len(word))
    words.append(word)

words = [("*" * (max_length-len(word))) + word for word in words]

char_dict = defaultdict(int)

for word in words:
    for i, char in enumerate(word):
        if char == "*": continue
        char_dict[char] += pow(10, max_length-i-1)

cnt = 9
answer = 0
for k, v in sorted(char_dict.items(), key=lambda x: -x[1]):
    answer += v * cnt
    cnt -= 1

print(answer)