L = int(input())
string = input()

r = 31
M = 1234567891

answer= 0
for i, char in enumerate(list(string)):
    answer += (ord(char)-96)*(r**i)%M

print(answer%M)
