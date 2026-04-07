# 트럭 하나로 배달/수거를 모두 마치고 물류창고에 돌아오는 최소 이동 거리

# 1. 가장 먼 곳부터 찍고 돌아오는 것이 최단거리이다.
# 2. 가장 먼 곳 순으로 택배 배달 후 픽업을 반복한다.
# 2-1. 가장 먼 배달/픽업 지점 확인
# 2-2. 최대로 배달 후 픽업
# 3. 거리 계산은 배달/픽업 인덱스 중 더 큰 인덱스를 누적하고 마지막에 *2 후 리턴

# N = 100000, 3*N -> O(N)

def findLast(m, arr):
    while m > 0 and arr[m - 1] == 0:
        m -= 1
    return m - 1

def work(cap, t, arr):
    last = -1
    for i in range(t, -1, -1):
        amount = min(arr[i], cap)
        arr[i] -= amount
        cap -= amount
        if cap <= 0: 
            return i + 1
    return 0

def solution(cap, n, deliveries, pickups):
    ans = 0
    md, mp = n, n
    while md + mp > 0:
        id = findLast(md, deliveries)
        ip = findLast(mp, pickups)
        
        md = work(cap, id, deliveries)
        mp = work(cap, ip, pickups)
        
        ans += (max(id + 1, ip + 1)) * 2
        
    return ans