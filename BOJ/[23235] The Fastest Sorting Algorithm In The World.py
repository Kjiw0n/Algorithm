arr = []
while True:
    a = list(map(int, input().split()))
    if a[0] == 0:
        break
    arr.append(a)

N = len(arr)
for i in range(N):
    print(f"Case {i + 1}: Sorting... done!")