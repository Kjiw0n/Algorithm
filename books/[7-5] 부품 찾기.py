N = int(input())
arr = list(map(int, input().split()))

M = int(input())
order_list = list(map(int, input().split()))

arr.sort()

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            return 'yes'
        elif target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 'no'

for o in order_list:
    print(binary_search(arr, o, 0, N-1), end=' ')

