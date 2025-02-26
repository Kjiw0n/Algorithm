loc = input()
x, y = ord(loc[0]) - 97, int(loc[1]) - 1 # 0, 0 기준
# print(x, y)

graph = [[0] * 8 for _ in range(8)]

dx = [-2, 2, -2, 2, -1, 1, -1, 1]
dy = [-1, 1, 1, -1, -2, 2, 2, -2]

cnt = 0
for dx, dy in zip(dx, dy):
    nx = x + dx
    ny = y + dy
    if 0 <= nx < 8 and 0 <= ny < 8:
        cnt += 1

print(cnt)