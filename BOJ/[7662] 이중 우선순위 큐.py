# 1. 삽입 (같은 수 삽입 가능)
# 2. 삭제
#     a. 최댓값 삭제
#     b. 최솟값 삭제
import collections
import sys
import heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    count = collections.defaultdict(int)

    min_pq = []
    max_pq = []

    def clear(pq, h):
        while pq and not count[pq[0] * h]:
            heapq.heappop(pq)

    for _ in range(k):
        s, n = map(str, input().split())
        n = int(n)

        if s == "I":
            if not count[n]:
                heapq.heappush(min_pq, n)
                heapq.heappush(max_pq, -n)
            count[n] += 1
        else:
            if n == -1:
                clear(min_pq, 1)
                if min_pq:
                    count[min_pq[0]] -= 1
                    while min_pq and count[min_pq[0]] == 0:
                        heapq.heappop(min_pq)
            else:
                clear(max_pq, -1)
                if max_pq:
                    count[-max_pq[0]] -= 1
                    while max_pq and count[-max_pq[0]] == 0:
                        heapq.heappop(max_pq)

    clear(min_pq, 1)
    clear(max_pq, -1)

    if min_pq and max_pq:
        print(-max_pq[0], min_pq[0])
    else:
        print("EMPTY")
