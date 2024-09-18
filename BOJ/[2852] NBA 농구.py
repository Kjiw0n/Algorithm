import sys

input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    team_num, time = map(str, input().split())
    arr.append([int(team_num), int(time[:2]), int(time[3:])])
arr.append([0, 48, 0])

win_time = [[0, 0], [0, 0]]
current_score = [0, 0] # [팀1, 팀2]

# 이기고있는 시간 계산
def time_func(t, i):
    for j in range(2):
        win_time[t][j] += (arr[i][j + 1] - arr[i - 1][j + 1])

# 스코어가 바뀔 때마다 체크
i = 0
while i < N + 1:
    if current_score[0] > current_score[1]:
        # 팀1이 이기고있음
        time_func(0, i)
    elif current_score[0] < current_score[1]:
        # 팀2이 이기고있음
        time_func(1, i)

    if arr[i][0] == 1:
        current_score[0] += 1
    elif arr[i][0] == 2:
        current_score[1] += 1

    i += 1

# print('팀1: ', win_time[0])
# print('팀2: ', win_time[1])

# 시간 변환
for i in range(2):
    while win_time[i][1] < 0:
        win_time[i][0] -= 1
        win_time[i][1] = 60 + win_time[i][1]

    if win_time[i][1] > 59:
        win_time[i][0] += (win_time[i][1] // 60)
        win_time[i][1] %= 60

    for j in range(2):
        win_time[i][j] = str(win_time[i][j])
        if len(win_time[i][j]) < 2:
            win_time[i][j] = '0' + win_time[i][j]

    print(win_time[i][0] + ':' + win_time[i][1])
