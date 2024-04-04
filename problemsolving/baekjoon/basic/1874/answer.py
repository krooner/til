n = int(input())

series = [int(input()) for _ in range(n)]

stack = []
orders = []
series_idx = 0
start = 1
while series_idx < n:
    target = series[series_idx]

    while start <= target:
        orders.append('push')
        stack.append(start)
        start += 1
    
    top = stack[-1] # 4
    if top == target: # 3
        orders.append('pop')
        stack.pop()
        series_idx += 1
    
    if top > target:
        orders = ['']
        break
        
for item in orders:
    if item == 'push':
        print("+")
    elif item == 'pop':
        print("-")
    else:
        print("NO")
