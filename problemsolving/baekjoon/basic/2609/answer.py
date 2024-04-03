a, b = map(int, input().split())

def gcd(a, b):
    while a%b >0:
        r = a%b
        a = b
        b = r
    return b

print(gcd(a, b))
print(a*b//gcd(a, b))