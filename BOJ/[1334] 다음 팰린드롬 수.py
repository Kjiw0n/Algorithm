N = input()

count = len(N)
# 반으로 나눠서 뒤집어서 붙이기
# -> 기존 숫자보다 작으면 가운데숫자만 커지게
# -> 더 못키우면 앞 절반에 +1

if count % 2 == 0:
    n1 = N[:(count // 2)]

    if N.count('9') == len(N):
        # N이 9로만 이루어졌으면
        result = '1' + '0' * (len(N) - 1) + '1'
    else:
        result = n1 + ''.join(reversed(n1))
        if result <= N:
            # 점점 키워야함
            n1 = str(int(n1) + 1)
            result = n1 + ''.join(reversed(n1))

    print(result)
else:
    n1 = N[:(count - 1) // 2]
    midN = N[(count - 1) // 2]

    if N.count('9') == len(N):
        # N이 9로만 이루어졌으면
        result = '1' + '0' * (len(N) - 1) + '1'
    else:
        result = n1 + midN + ''.join(reversed(n1))

        if result <= N:
            if int(midN) == 9:
                n1 = str(int(n1) + 1)
                result = n1 + '0' + ''.join(reversed(n1))
            else:
                midN = str(int(midN) + 1)
                result = n1 + midN + ''.join(reversed(n1))

    print(result)
