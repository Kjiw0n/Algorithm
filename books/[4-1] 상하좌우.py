# (1, 1)은 (0, 0)이라고 생각할거임.
# : 각 좌표에서 1씩 빼서 계산

N = int(input())
A = list(input().split())

# 책 풀이)
#  L, R, U D를 하나의 리스트에 넣고, dx(: L, R), dy(: U, D)라는 변수에 각 방향 설정
#  direction = ['L', 'R', 'U', 'D']
#  dx = [0, 0, -1, 1] #: 여기서 x는 수학에서의 x축 방향이 아니다... 이거땜에 헷갈렸다. 행렬에서의 x임 (세로)
#  dy = [-1, 1, 0, 0] #: 따라서 여기서 y는 행렬에서의 y (가로)
# A를 for문 돌려서 i에 해당하는 direction이 같을 경우 -> dx, dy 더해줌

status = [0, 0]
for a in A:
  if a == 'L':
    if status[1] - 1 >= 0:
      status[1] -= 1
  elif a == 'R':
    if status[1] + 1 < N:
      status[1] += 1
  elif a == 'U':
    if status[0] - 1 >= 0:
      status[0] -= 1
  else: # a == 'D'
    if status[0] + 1 < N:
      status[0] += 1

status[0] += 1
status[1] += 1
print(*status)