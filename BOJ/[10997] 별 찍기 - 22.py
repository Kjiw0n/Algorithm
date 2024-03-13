# 1 1
# 2 5
# 3 9
# 4 13
# -> 4씩 커짐. 4n-3
# 세로도 똑같음 (안겹치게 셀 때)

# 중간 기점으로 규칙 세서 풂

N = int(input())
sequence = 4 * N - 3
ss = sequence + 1
half = ((sequence + 1) // 2)

if N == 1:
    print('*')
else:
    first = '* '
    end = ' *'
    for i in range(half):
        if i % 2 == 0:
            if i == 0:
                print('*' * (ss - 1))
                ss -= 2
            else:
                fn = i // 2
                en = fn - 1
                mn = ss - fn - en
                print(first * fn + '*' * mn + end * en)
                ss -= 2
        else:
            if i == 1:
                print('*')
            else:
                fn = (i + 1) // 2
                en = fn - 1
                mn = ss - (fn + en)
                print(first * fn + ' ' * mn + end * en)

    # print('ss: ', ss)
    print('* ' * ((sequence + 1) // 2))
    # print('---')

    for i in range(half):
        if i % 2 == 0:
            fn = ss // 2
            en = fn
            mn = sequence - ((fn + en) * 2)
            # print('fn: ', fn, 'en: ', en, 'mn: ', mn)
            print(first * fn + '*' * mn + end * en)
        else:
            fn = ss // 2
            en = fn
            mn = sequence - ((fn + en) * 2)
            print(first * fn + ' ' * mn + end * en)
            ss -= 2
