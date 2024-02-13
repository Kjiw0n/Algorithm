# 합 총개수 시작숫자 개수
# 2 (1) N~ 1
# 3 (2) 1~ 2~3
# 4 (3) N~ 4~6
# 5 (4) 1~ 7~10
# 6 (5) N~ 11~15
# ...
# 같은 대각선에 있으면 합 같음

X = int(input())

i = 0 # : 개수
N = 1 # : 총 개수
start = 0
order = 0
while True:
    i += N

    if X <= i:
        if N % 2 != 0:
            # N 홀수
            start = N
            order = (N - (i - X)) - 1
            a = start - order
        else:
            # N 짝수
            start = 1
            order = (N - (i - X)) - 1
            a = start + order

        b = (N + 1) - a
        result = str(a) + '/' + str(b)
        print(result)
        break

    N += 1