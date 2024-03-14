n, m = map(int, input().split())

# 입력 시 무조건 n이 m보다 커야함
def rectangle(n, m, count):
    print('n:', n, 'm:', m, 'count:', count)
    if n % m == 0:
        # 이러면 끝임
        count += n // m
        print(count)
        return
    else:
        count += n // m
        rectangle(m, n % m, count)

if n >= m:
    rectangle(n, m, 0)
else:
    rectangle(m, n, 0)
