arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr) - 1):
    print('i: ', i, 'arr[i + 1:len(arr)]: ', arr[(i + 1):len(arr)])
    if arr[i] > min(arr[(i + 1):len(arr)]):
        print('min(arr[(i + 1):len(arr)]): ', min(arr[(i + 1):len(arr)]))
        min_index = arr.index(min(arr[(i + 1):len(arr)]))
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)

print(arr)