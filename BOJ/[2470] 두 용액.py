N = int(input())

arr = list(map(int, input().split()))
arr.sort()
print(arr)

start = 0
end = N - 1

value = abs(arr[start] - arr[end])
result = [arr[start], arr[end]]

while start < end:
    start_n = arr[start]
    end_n = arr[end]

    sum = start_n - end_n
    if abs(sum) < value:
        value = abs(sum)
        if value == 0:
            break

    if sum < 0:
        start += 1
    else:
        end -= 1

print(*result)
