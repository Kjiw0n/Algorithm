from collections import deque


def solution(dirs):
    # 방향 최댓값 11

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dirs = list(dirs)

    def direction(d):
        if d == 'U':
            return 0
        elif d == 'D':
            return 1
        elif d == 'R':
            return 3
        elif d == 'L':
            return 2

    visit = set()
    i, j = 5, 5
    answer = 0
    for d in dirs:
        di = i + dx[direction(d)]
        dj = j + dy[direction(d)]
        print(d, di, dj)

        if 0 <= di < 11 and 0 <= dj < 11:
            if ((i, j), (di, dj)) not in visit:
                answer += 1
                visit.add(((i, j), (di, dj)))
                visit.add(((di, dj), (i, j)))
            i, j = di, dj

    return answer

print(solution('ULURRDLLU'))
print(solution('LULLLLLLU'))
