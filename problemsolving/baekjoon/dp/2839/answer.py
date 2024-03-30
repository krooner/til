N = int(input())

dp_table = [10000] * 5001

dp_table[3] = 1
dp_table[5] = 1

def count_bag(left):
    
    for i in range(5, left+1):

        opt_1 = i-3       
        dp_table[i] = min(dp_table[i], 1+dp_table[opt_1])

        opt_2 = i-5
        dp_table[i] = min(dp_table[i], 1+dp_table[opt_2])

    return dp_table[left]

answer = count_bag(N)
if answer == 10000:
    print(-1)
else:
    print(answer)