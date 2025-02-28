def binary(target, start, end):
    if start > end:
        return None
    print(start, end)
    mid = (start + end) // 2
    print('ㅜㅜ', target, arr[mid])
    if target == arr[mid]:
        return mid
    elif target > arr[mid]:
        return binary(target, mid + 1, end)
    else:
        return binary(target, start, mid - 1)

n, target = map(int, input().split())
arr = list(map(int, input().split()))

result = binary(target, 0, n - 1)
if result == None:
    print('원소 존재 x')
else:
    print(result + 1)
