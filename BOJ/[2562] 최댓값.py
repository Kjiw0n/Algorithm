arr = []
for _ in range(9):
    arr.append(int(input()))

m = max(arr)
m_index = arr.index(m)

print(m)
print(m_index + 1)