from itertools import combinations

arr = []
for _ in range(9):
    arr.append(int(input()))

result = 0
comb = list(combinations(arr, 7))
for c in comb:
    if sum(c) == 100:
        result = sorted(c)
        break
for r in result:
    print(r)