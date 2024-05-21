while True:
    strlist = list(map(str, input().split()))
    if strlist[0] == '#':
        break

    if int(strlist[1]) > 17 or int(strlist[2]) >= 80:
        print(strlist[0], 'Senior')
    else:
        print(strlist[0], 'Junior')
