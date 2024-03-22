def solution(citations):
    arr = sorted(citations)

    l = len(arr)
    h = max(arr) if max(arr) <= l else l
    if h != 0:
        while h >= 0:
            if arr[l - h] >= h:
                break
            h -= 1

    answer = h
    return answer