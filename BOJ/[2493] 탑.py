N = int(input())

arr = list(map(int, input().split()))
# print(arr)

# 스택에 인덱스도 같이 넣기
# 나보다 작은 걸 pop하기 (순서대로 push하니까 나보다 작은 건 필요없음)
stack = []
result = []
for i in range(N):
    while stack and stack[-1][0] <= arr[i]:
        stack.pop()
    result.append(stack[-1][1] + 1 if stack else 0)
    stack.append((arr[i], i))

print(*result)
