N = int(input())
set_n = set(map(int, input().split()))

M = int(input())
arr = list(map(int, input().split()))

for a in arr:
    if a in set_n:
        print(1)
    else:
        print(0)
