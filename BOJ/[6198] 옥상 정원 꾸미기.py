# 모든 빌딩은 일렬로 서 있고 오른쪽으로만 볼 수 있다.
import sys

input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    arr.append(int(input()))

stack = []
count = 0
for a in arr:
    while stack and stack[-1] <= a:
        stack.pop()

    count += len(stack)
    stack.append(a)
    # print(stack)

print(count)
