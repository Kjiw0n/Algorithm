import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# if max_index == N - 1:
#     # 최댓값이 맨 끝 -> 젤 간단 다 빼면 끝
# else:
#     # 최댓값이 중간 또는 맨 앞 -> 최댓값까지는 if문과 동일, 최댓값 이후부터는 다시 재귀 느낌으로 제일 큰 값 찾기?
    #
    # 그냥 단순하게
    # 뒤에 더 큰 값 없으면 사지마
    # 더 큰 값 있으면 사고 그 값에서 팔아 (remain 중 max 값 유의)
    # if문이 필요없네

# result = 0
# while arr:
#     # arr가 전부 사라질 때 까지
#     max_value = max(arr)
#     max_index = arr.index(max_value)
#
#     for _ in range(max_index):
#         result += (max_value - arr[0])
#         # print('result: ', result)
#         arr.pop(0)
#     # print(arr)
#
#     if max_index == 0:
#         arr.pop(0)

# 개선버전
max_value = 0
result = 0
for i in range(N - 1, -1, -1):
    if arr[i] > max_value:
        max_value = arr[i]
    result += (max_value - arr[i])

print(result)
