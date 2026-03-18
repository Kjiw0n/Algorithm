# Todo: 수빈이가 동생을 가장 빠르게 찾기
# return: 가장 빠른 시간, 가장 빠른 방법 가짓수

# 1. 수빈이와 동생의 위치 입력받기
# 2. 동생과의 최단 거리 구하기
#     1. 동생을 찾는 가장 빠른 시간 == 동생과의 최단 거리
#     2. 수빈이 이동 방법 3가지 (X-1, X+1, X*2)로 이동
# 3. 최솟값 찾기
# 
# 동생과의 최단거리를 판별할 때, 방문하지 않은 노드만 탐색하는 것이 아닌 최소시간을 저장(visited → dist, cnt)
# dist[x] = x에 도착한 최소 시간
# cnt[x] = 최소 시간으로 x에 방문하는 횟수
# 1. 방문하지 않았을 경우: 최소시간, 방문횟수 업데이트
# 2. 이미 방문한 최소 경로를 거치는 경우: 방문횟수만큼 더함 (누적 횟수 카운트)

from collections import deque

N, K = map(int, input().split())
dist = [-1] * 100001
cnt = [0] * 100001

def bfs(N):
    queue = deque()
    queue.append(N)
    dist[N] = 0
    cnt[N] = 1
    while queue:
        q = queue.popleft()
        for nq in (q - 1, q + 1, q * 2):
            if 0 <= nq <= 100000:
                if dist[nq] == -1:
                    dist[nq] = dist[q] + 1
                    cnt[nq] = cnt[q]
                    queue.append(nq)
                elif dist[nq] == dist[q] + 1:
                    cnt[nq] += cnt[q]

bfs(N)
print(dist[K])
print(cnt[K])
