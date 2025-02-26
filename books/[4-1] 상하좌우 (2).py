N = int(input())
arr = list(map(str, input().split()))

loc = [1, 1]

def isMove(x, y):
    if 0 < x <= N and 0 < y <= N:
        return True
    return False

for a in arr:
    if a == 'U':
        if isMove(loc[0] - 1, loc[1]):
            loc[0] -= 1
    elif a == 'D':
        if isMove(loc[0] + 1, loc[1]):
            loc[0] += 1
    elif a == 'L':
        if isMove(loc[0], loc[1] - 1):
            loc[1] -= 1
    elif a == 'R':
        if isMove(loc[0], loc[1] + 1):
            loc[1] += 1

print(*loc)

# 5
# R R R U D D