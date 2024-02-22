# s 01:01 (15분)
# e 01:07

N = int(input())

array = []
for _ in range(N):
    array.append(int(input()))

# sol1)
# array.sort()
# array.reverse()

# sol2)
array = sorted(array, reverse=True)

print(*array)