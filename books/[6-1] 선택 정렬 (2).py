arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)):
    idx = i
    for j in range(i, len(arr)):
        if arr[idx] > arr[j]:
            idx = j
    arr[i], arr[idx] = arr[idx], arr[i]

print(arr)