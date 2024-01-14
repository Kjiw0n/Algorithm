import sys

result = []

for _ in range(3):
    n = int(sys.stdin.readline())
    total = 0
    for _ in range(n):
        total += int(sys.stdin.readline().strip())

    if total > 0:
        result.append('+')
    elif total == 0:
        result.append('0')
    else:
        result.append('-')

print('\n'.join(result))