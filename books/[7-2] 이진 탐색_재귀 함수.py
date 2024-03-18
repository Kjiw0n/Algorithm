def binary_search(arr, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        end = mid - 1
        return binary_search(arr, target, start, end)
    else:
        start = mid + 1
        return binary_search(arr, target, start, end)

n, target = map(int, input().split())
arr = list(map(int, input().split()))

result = binary_search(arr, target, 0, n - 1)
if result == None:
    print('원소 존재 x')
else:
    print(result + 1)

