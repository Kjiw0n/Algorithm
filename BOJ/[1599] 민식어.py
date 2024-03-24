N = int(input())

arr = []
for _ in range(N):
    arr.append(input())

# 'ng' -> 'x'로 바꾸기 (한 문자로 처리해야 정렬 가능)
for i in range(len(arr)):
    if arr[i].count('ng') > 0:
        # print(arr[i], i)
        a = list(arr[i])
        for j in range(1, len(a)):
            if a[j - 1] == 'n' and a[j] == 'g':
                a[j - 1], a[j] = 'x', ''
        arr[i] = ''.join(a)
        # print(arr[i])

# print('정렬 전 arr: ', arr)

language = ['a', 'b', 'k', 'd', 'e', 'g', 'h', 'i', 'l', 'm', 'n', 'x', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y']

arr.sort(key=lambda x: [language.index(c) for c in x])

# 'x' -> 'ng'로 다시 변경
# print("'x' -> 'ng'로 다시 변경")
for i in range(len(arr)):
    if arr[i].count('x') > 0:
        a = list(arr[i])
        for j in range(len(a)):
            if a[j] == 'x':
                a[j] = 'ng'
        arr[i] = ''.join(a)
        # print(arr[i])

for a in arr:
    print(a)
