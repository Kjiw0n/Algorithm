def isPellin(n):
    l = len(str(n))
    arr = list(str(n))
    # print(arr)
    for i in range(l // 2):
        if arr[i] != arr[-(i + 1)]:
            return False
            # print('틀림', 'arr[i] != arr[-i]', arr[i], arr[-(i + 1)])

    return True


while True:
    n = int(input())
    if n == 0:
        break
    else:
        if isPellin(n):
            print('yes')
        else:
            print('no')