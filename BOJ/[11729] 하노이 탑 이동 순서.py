N = int(input())

res = []
def hanoi(n, start, mid, end):
    if n == 1:
       res.append((start, end))
       return
    hanoi(n - 1, start, end, mid)
    res.append((start, end))
    hanoi(n - 1, mid, start, end)

hanoi(N, 1, 2, 3)

print(len(res))
for r in res:
    print(*r)