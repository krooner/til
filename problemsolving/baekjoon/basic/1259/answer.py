while True:
    word = input()
    if word == '0': break

    length = len(word)

    flag = True
    for i in range(int(length/2)):
        lchar, rchar = word[i], word[length-1-i]
        if lchar != rchar:
            flag = False
            break
    
    print('yes' if flag else 'no')