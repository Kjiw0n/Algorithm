L, C = map(int, input().split())
arr = list(map(str, input().split()))
arr.sort()

vowel = ('a', 'e', 'i', 'o', 'u')

def dfs(pw, idx, a, b):
    if len(pw) >= L:
        # 조건 검사
        if a >= 1 and b >= 2:
            print(pw)
        return

    for i in range(idx, C):
        if arr[i] in vowel:
            dfs(pw + arr[i], i + 1, a + 1, b)
        else:
            dfs(pw + arr[i], i + 1, a, b + 1)

dfs('', 0, 0, 0)
