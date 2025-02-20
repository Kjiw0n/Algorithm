def solution(sizes):
    arr = []

    for s in sizes:
        arr.append([max(s), min(s)])

    w, h = map(max, zip(*arr))

    return w * h