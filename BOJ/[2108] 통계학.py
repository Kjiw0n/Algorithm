from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    arr.append(int(input()))

arr.sort()

print(round(sum(arr) / N))
print(arr[N // 2])

m = Counter(arr).most_common()
if N == 1:
    print(arr[0])
else:
    if m[0][1] == m[1][1]:
        print(m[1][0])
    else:
        print(m[0][0])

print(max(arr) - min(arr))

