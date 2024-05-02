arr = []
for _ in range(3):
    arr.append(int(input()))

total = arr[0] * arr[1] * arr[2]
# print(total)
result = [0] * 10
for t in str(total):
    result[int(t)] += 1

for r in result:
    print(r)