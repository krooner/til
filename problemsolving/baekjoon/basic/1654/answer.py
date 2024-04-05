from collections import deque

while True:
    line = input()
    if line == '.':
        break

    pts = deque([])

    flag = True
    for char in line:
        if char == '(':
            pts.append(char)
        elif char == ')':
            if len(pts) == 0:
                flag = False
                break
            else:
                if pts[-1] != '(':
                    flag = False
                    break
                else:
                    pts.pop()
        elif char == '[':
            pts.append(char)
        elif char == ']':
            if len(pts) == 0:
                flag = False
                break
            else:
                if pts[-1] != '[':
                    flag = False
                    break
                else:
                    pts.pop()

    if len(pts) != 0:
        flag = False
    
    if flag:
        print('yes')
    else:
        print('no')
