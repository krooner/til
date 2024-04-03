N = int(input())
A = sorted(map(int, input().split()))

def binary_search(num, left_idx, right_idx):
    if left_idx > right_idx: return False
    
    mid_idx = left_idx + (right_idx - left_idx)//2
    if A[mid_idx] == num:
        return True
    elif A[mid_idx] < num:
        return binary_search(num, mid_idx+1, right_idx)
    else:# A[mid_idx] < num: # A[mid_idx] < num
        return binary_search(num, left_idx, mid_idx-1)

M = int(input())
for item in map(int, input().split()):
    print(1 if binary_search(item, 0, N-1) else 0)