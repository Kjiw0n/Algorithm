nA, nB = map(int, input().split())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

arrA.sort()
arrB.sort()

def binary_search(a):
    s = 0
    e = len(arrB) - 1

    while s <= e:
        mid = (s + e) // 2

        if a < arrB[mid]:
            e = mid - 1
        elif a > arrB[mid]:
            s = mid + 1
        else:
            # a == arrB[mid]
            return a
    return None


# arrB에 포함되지 않는 A 찾기
# inc에는 arrB에 포함된 a를 넣자
inc = set()
for a in arrA:
    if binary_search(a) is not None:
        inc.add(a)

ans = [a for a in arrA if a not in inc]

if ans:
    print(len(ans))
    print(*ans)
else:
    print(0)
