from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

count_arr1 = Counter(arr1)
for a in arr2:
    print(count_arr1[a], end=' ')
