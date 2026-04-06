# return: 충돌 위험 상황이 발생하는 총 횟수

# 1. 각 로봇이 목적지로 이동하는 최단 경로 구하기
# 1-1. 상하좌우 이동만 가능하므로, 일정한 방향으로 가면 됨
# 1-2. 최단 경로가 여러가지인 경우, r 좌표 이동을 먼저 한다.
# 1-3. 최단 경로대로 움직인 좌표를 저장한다.
# 2. 같은 시간에 같은 위치에 있는 경우 카운트 (충돌하는 좌표를 세면 됨)

def solution(points, routes):    
    # 최단 경로 구하기
    shortest_path = []
    for route in routes:
        path = []
        s = route[0]
        prev = ()
        for r in route:
            e = r
            if s == e: continue
            start = points[s - 1]
            end = points[e - 1]
            
            now = ()
            
            if end[0] - start[0] > 0:
                for i in range(start[0], end[0] + 1):
                    now = (i, start[1])
                    if prev != now:
                        path.append(now)
                    prev = now
            elif end[0] - start[0] < 0:
                for i in range(start[0], end[0] - 1, -1):
                    now = (i, start[1])
                    if prev != now:
                        path.append(now)
                    prev = now

            if end[1] - start[1] > 0:
                for i in range(start[1], end[1] + 1):
                    now = (end[0], i)
                    if prev != now:
                        path.append(now)
                    prev = now
            elif end[1] - start[1] < 0:
                for i in range(start[1], end[1] - 1, -1):
                    now = (end[0], i)
                    if prev != now:
                        path.append(now)
                    prev = now
            s = r
            
        shortest_path.append(path)
    
    max_p = 0
    for path in shortest_path:
        max_p = max(max_p, len(path))
    
    # 1초에 1칸씩 이동하며 로봇 충돌하는 경우 카운트
    ans = 0
    t = 0
    
    while t < max_p:
        seen = set()
        dup = set()
        for path in shortest_path:
            if len(path) > t:
                if path[t] in seen:
                    dup.add(path[t])
                else:
                    seen.add(path[t])
        ans += len(dup)
        t += 1
    
    return ans