n = int(input())

def fibo_recursion(n):
    a = 1
    b = 1
    
    for _ in range(3, n+1):
        a, b = b, a+b
    
    return b
    
table = [None] * 41
def fibo_dp(n):
    answer = 0
    table[1] = 1
    table[2] = 1

    for i in range(3, n+1):
        answer += 1
        table[i] = table[i-1] + table[i-2]
    
    return answer

print(fibo_recursion(n), fibo_dp(n))