T = int(input())

# 최소공배수 = a * b / 최대공약수
def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

for _ in range(T):
    a, b = map(int, input().split())
    n = gcd(a, b)
    print(a // n * b)
