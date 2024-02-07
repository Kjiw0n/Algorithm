import sys
input = sys.stdin.readline

# 크레인 N대
# 각 크레인 무게 제한
# 박스 M개
# 각 박스의 무게
N = int(input())
limit_N = list(map(int, input().split()))
M = int(input())
weight_M = list(map(int, input().split()))

# 1분에 박스 하나씩 배에 실음 & 모든 크레인 동시에 움직임
# 각 크레인 무게 제한 있음
# 모든 박스 옮기는 최소 시간은?

# 큰 순으로 정렬 (크레인, 박스 둘 다)
# 넣을 수 있는만치 넣고
# 안되면 다음 턴 (1분 추가)

result = 0
limit_N = sorted(limit_N, reverse=True)
weight_M = sorted(weight_M, reverse=True)

if limit_N[0] < weight_M[0]:
    print(-1)
    sys.exit()

# 크레인이 박스 들 수 있으면 그 박스 들고, 못드는 인덱스까지 가면 다시 처음부터 반복
while len(weight_M):
    for i in range(len(limit_N)):
        for j in range(len(weight_M)):
            if limit_N[i] >= weight_M[j]:
                weight_M.remove(weight_M[j])
                break
    result += 1

print(result)