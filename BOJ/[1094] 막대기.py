X = int(input())

# 가장 짧은 것을 절반으로 자름 -> min(arr) // 2
# if (min(arr) // 2) + arr - min(arr) >= X: arr.pop(min(arr)) and arr.append(min(arr)//2)
# if sum(arr) == X: done, else: recursive

arr = [64]

while sum(arr) > X:
    arr.sort(reverse=True) # descending order
    m = arr[len(arr) - 1]

    if (m // 2) + sum(arr) - m >= X:
        arr.pop(len(arr) - 1)
        arr.append(m // 2)
    else:
        arr.pop(len(arr) - 1)
        arr.append(m // 2)
        arr.append(m // 2)

print(len(arr))

