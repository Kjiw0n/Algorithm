T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = 0

    A.sort()
    B.sort()

    for a in A:
        s = 0
        e = M - 1
        cnt = -1
        while s <= e:
            m = (s + e) // 2
            if B[m] < a:
                # print('a: ', a, 'B[m]: ', B[m], 'm: ', m)
                cnt = m
                s = m + 1
            else:
                e = m - 1
        # print('a: ', a, 'cnt: ', cnt)


        # if cnt + 1 == M:
        #     # a 뒤에 애들도 다 M일거임
        #     print(a)
        result += (cnt + 1)

    print(result)

