N = int(input())
for i in range(N):
    arr = input().split()
    print(f"Case #{i + 1}: {' '.join(arr[::-1])}")
