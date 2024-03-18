import sys

arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

result_arr = [0] * (max(arr) + 1)

for i in range(len(arr)):
    result_arr[arr[i]] += 1

print(result_arr)

for i in range(len(result_arr)):
    for j in range(result_arr[i]):
        print(i, end=' ')