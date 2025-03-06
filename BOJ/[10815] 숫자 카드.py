import sys

input = sys.stdin.readline

N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

def bisect_search(n, s, e):
    if s > e:
        return False
    mid = (s + e) // 2

    if n == arr1[mid]:
        return True
    elif n > arr1[mid]:
        return bisect_search(n, mid + 1, e)
    else:
        return bisect_search(n, s, mid - 1)

arr1.sort()
for a in arr2:
    if bisect_search(a, 0, N - 1):
        print(1, end=' ')
    else:
        print(0, end=' ')
