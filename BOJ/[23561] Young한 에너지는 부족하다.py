import sys

N = int(sys.stdin.readline())

crew_num = 3 * N
age = [0] * N

age = list(map(int, sys.stdin.readline().split()))

# 각 크루의 중간값만 알면 됨
# 크루원은 무조건 3명씩
# N개의 중간값 나올거임. N명만 찾으면 됨
# sort 했을 때 중간 N개?
# 그 중 '가장 큰 중간값 - 가장 작은 중간값' 비교

sorted_age = sorted(age)

# sorted_age[N]이랑 sorted_age[2N-1]만 찾으면 됨
# resultt = sorted_age[2N-1] - sorted_age[N]

result = sorted_age[2 * N - 1] - sorted_age[N]
print(result)