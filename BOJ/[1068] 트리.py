N = int(input())
tree = list(map(int, input().split()))
d = int(input())

# 인접리스트로 풀어 -> 비어있는 애들만 카운트
arr = [[] for _ in range(N)]
# print(arr)
root = 0
for i in range(N):
    if tree[i] == -1:
        root = i
        continue
    arr[tree[i]].append(i)

# print(arr)

# dfs 재귀로 풀기
visited = [False] * N
cnt = [0]
def dfs(v):
    # print(v, 'is in dfs')
    visited[v] = True
    if not arr[v]:
        # 리프 노드라는 소리
        # print(v, 'is leaf')
        cnt[0] += 1
        return
    for a in arr[v]:
        # print('a: ', a)
        # 연결된 애들 다 돌기
        if not visited[a]:
            dfs(a)

if d == root:
    print(0)
else:
    # 삭제노트를 미리 다 지우고 하자
    for i in range(N):
        if d in arr[i]:
            arr[i].remove(d)
    dfs(root)
    print(cnt[0])