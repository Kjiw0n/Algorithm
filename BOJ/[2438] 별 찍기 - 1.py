import sys

N = int(input())

for i in range(1, N + 1):
    for _ in range(i):
        sys.stdout.write('*')
    i += 1
    print()