import heapq
import sys
input = sys.stdin.readline
# 현재 선물이 가장 많이 담겨있는 상자에서
# 상자에 자신이 원하는 것보다 적은 개수의 선물이 들어있다면, 선물을 가져가지 못해 실망

N, M = map(int, input().split())

presents = list(map(int, input().split()))
children = list(map(int, input().split()))

# print('presents: ', presents)
# print('children: ', children)

# presents를 힙큐로 받아야하나? -> 최대힙으로 저장하고
# 가장 큰 값과 children을 비교하는거임

heap = []

for p in presents:
    heapq.heappush(heap, -p)

# print(heap)

result = 1
for c in children:

    h = -heapq.heappop(heap)

    # print('heap[0], c: ', -heap[0], c)

    if h > c:
        h -= c
        heapq.heappush(heap, -h)
    elif h == c:
        continue
    else:
        result = 0
        break

    # print('heap: ', heap)

print(result)
