def solution(n, lost, reserve):
    lost_info = lost
    reserve_info = reserve
    lost = sorted([l for l in lost if l not in reserve_info])
    reserve = sorted([r for r in reserve if r not in lost_info])

    arr = []
    for l in lost:
        if l - 1 in reserve:
            reserve.remove(l - 1)
        elif l + 1 in reserve:
            reserve.remove(l + 1)
        else:
            arr.append(l)

    ans = n - len(arr)
    return ans