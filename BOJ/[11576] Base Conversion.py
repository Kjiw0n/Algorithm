A, B = map(int, input().split())
m = int(input())
arr = list(map(int, input().split()))

n = 0
for i in range(len(arr)):
    m -= 1
    n += arr[i] * (A ** m)

result = []
while n // B != 0:
    result.append(n % B)
    n //= B

result.append(n)

for i in range(len(result) - 1, -1, -1):
    print(result[i], end=' ')