A, B, V = map(int, input().split())

q, r = divmod((V-A), (-B+A))
if r == 0:
    print(q+1)
else:
    print(q+1+1)

#A + (-B+A)*N >= V
#(V - A)/(-B+A) =< N