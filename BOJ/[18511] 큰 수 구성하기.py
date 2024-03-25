from itertools import product

N, K = map(int, input().split())

# K 최댓값이 3(최대 27 + 12 + 3개) -> 하나씩 비교해도 됨
length_n = len(str(N))
arr = list(map(int, input().split()))

max_num = 0
for k in range(1, length_n + 1):
    for a in product(arr, repeat=k):
        num = ''
        for i in range(len(a)):
            num += str(a[i])
        num = int(num)
        if max_num < num <= N:
            max_num = num

print(max_num)