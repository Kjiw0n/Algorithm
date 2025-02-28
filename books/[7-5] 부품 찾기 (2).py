import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
M = int(input())
arr_m = list(map(int, input().split()))
arr.sort()

def binary_search(target, s, e):
    if s > e:
        return False
    mid = (s + e) // 2
    if target == arr[mid]:
        return True
    elif target > arr[mid]:
        return binary_search(target, mid + 1, e)
    else:
        return binary_search(target, s, mid - 1)

for a in arr_m:
    if binary_search(a, 0, len(arr) - 1):
        print('yes', end=' ')
    else:
        print('no', end=' ')