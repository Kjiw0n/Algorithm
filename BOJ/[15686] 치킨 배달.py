# N x N
# 0은 빈 칸, 1은 집, 2는 치킨집

# 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리
# 치킨 거리는 집을 기준으로 정해지며
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합

# 집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재
# 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.

from itertools import combinations

# M: 남길 치킨집 수
N, M = map(int, input().split())

graph = []
for _ in range(N):
    arr = list(map(int, input().split()))
    graph.append(arr)

c_arr = [] # : 치킨집 주소 저장
h_arr = [] # : 집 주소 저장
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            c_arr.append([i, j])
        elif graph[i][j] == 1:
            h_arr.append([i, j])

length = [] # 치킨거리
result = 0
for h in h_arr:
    l = []
    for c in c_arr:
        l.append(abs(c[0] - h[0]) + abs(c[1] - h[1]))
    result += min(l)
    length.append(l)

if len(c_arr) != M:
    # M 개의 치킨집 살릴거임. c_arr에서 인덱스 M개 뽑아서 min(l) 합했을 때 가장 작은 경우
    combination = combinations(list(range(len(c_arr))), M)
    min_sum = 50 * 50 * 50 * 13 # 얘를 어케 초기화하지.....
    for comb in combination:
        temp = 0
        # print('comb: ', comb)
        for l in length:
            temp_arr = []
            for i in range(len(comb)):
                temp_arr.append(l[comb[i]])
            temp += min(temp_arr)
        if temp < min_sum:
            min_sum = temp

    result = min_sum

print(result)

