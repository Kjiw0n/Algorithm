import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# 정렬 한 다음에 각 값끼리 비교하는 게 아니라 해당 인덱스를 출력하면 될듯
comp_arr = sorted(list(set(arr)))
dict_arr = {comp_arr[i] : i for i in range(len(comp_arr))}
for a in arr:
    print(dict_arr[a], end=' ')
