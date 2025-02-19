import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

stack = [0]
for a in arr:
    while stack and stack[-1] <= a:
        stack.pop()
    if not stack or stack[-1] != a:
        stack.append(a)

print(len(stack))
