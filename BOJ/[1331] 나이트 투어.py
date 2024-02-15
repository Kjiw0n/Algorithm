# x축 대칭 시켜서 생각해도 될거같다

route_list = []
# ord('A'): 65, ord('B'): 66
for i in range(36):
    route = input()
    route_list.append([ord(route[0]) - 65, int(route[1]) - 1])

start_x = route_list[0][0]
start_y = route_list[0][1]

# 6 x 6
visit = [[0] * 6 for _ in range(6)] # 0: 방문x, 1: 방문o

# 나이트 이동 방법 8가지 -> abs(): 절대값 변환 함수 (!!)

result = True
for i in range(36):
    x, y = route_list[i][0], route_list[i][1]
    if visit[x][y] == 0:
        # 방문하지 않았다면, 방문 처리
        visit[x][y] = 1

        # 가능한 경로였는 지 판단
        if i > 0:
            prev_x, prev_y = route_list[i - 1]
            if not ((abs(prev_x - x), abs(prev_y - y)) in [(1, 2), (2, 1)]):
                result = False
                break
    else:
        # 이미 방문한 곳이였다면, Invalid 처리
        result = False
        break

if result:
    # 마지막 칸에서 처음으로 갈 수 있는 지
    end_x, end_y = route_list[-1][0], route_list[-1][1]
    if not ((abs(end_x - start_x), abs(end_y - start_y)) in [(1, 2), (2, 1)]):
        result = False

# 다 돌아도 시간 초과x 니까 모든 경로 검사 후 출력
if result:
    print("Valid")
else:
    print("Invalid")
