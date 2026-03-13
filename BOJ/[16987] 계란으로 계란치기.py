# 각 계란에는 내구도와 무게가 정해져있다.
# 계란으로 계란을 치게 되면 각 계란의 내구도는 상대 계란의 무게만큼 깎이게 된다.
# 그리고 내구도가 0 이하가 되는 순간 계란은 깨지게 된다.

# 왼쪽부터 차례로 들어서 한 번씩만 다른 계란을 쳐 최대한 많은 계란을 깨는 문제

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

maxN = 0
def dfs(start, cnt, li):
    if start == N:
        global maxN
        maxN = max(maxN, cnt)
        return

    if li[start][0] <= 0:
        dfs(start + 1, cnt, li)
        return
    # 계란 깨기 (start -> i)
    flag = False
    for i in range(N):
        if start != i and li[i][0] > 0:
            flag = True
            broken = 0
            li[start][0] -= li[i][1]
            li[i][0] -= li[start][1]
            if li[i][0] <= 0: broken += 1
            if li[start][0] <= 0: broken += 1
            dfs(start + 1, cnt + broken, li)
            li[start][0] += li[i][1]
            li[i][0] += li[start][1]
    if not flag:
        dfs(start + 1, cnt, li)

dfs(0, 0, arr)

print(maxN)
