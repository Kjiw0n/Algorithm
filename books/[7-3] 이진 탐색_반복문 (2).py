n, target = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = n - 1

ans = len(arr)
while start <= end:
    mid = (start + end) // 2
    if target == arr[mid]:
        ans = mid + 1
        break
    elif target > arr[mid]:
        start = mid + 1
    else:
        end = mid - 1

if ans == len(arr):
    print('원소 존재 x')
else:
    print(ans)