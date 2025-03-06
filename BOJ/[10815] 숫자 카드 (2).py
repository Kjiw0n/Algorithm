import sys

input = sys.stdin.readline

N = int(input())
arr1 = set(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

print(' '.join('1' if a in arr1 else '0' for a in arr2))
