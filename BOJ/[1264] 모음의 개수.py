while True:
    str1 = input()
    if str1 == '#':
        break
    vowel = 'aeiouAEIOU'

    cnt = 0
    for s in str1:
        if s in vowel:
            cnt += 1

    print(cnt)