def toStrUnder10(n):
    if n < 10:
        n = '0' + str(n)
    else:
        n = str(n)
    return n


def solution(video_len, pos, op_start, op_end, commands):
    # 다 초 단위로 변환
    arr = video_len, pos, op_start, op_end
    arrL = []
    arrI = []
    for a in arr:
        arrL.append(list(map(int, a.split(':'))))
    for a in arrL:
        arrI.append(a[0] * 60 + a[1])

    video_lenI = arrI[0]
    posI = arrI[1]
    op_startI = arrI[2]
    op_endI = arrI[3]

    # 오프닝 건너뛰기 자동 실행
    if op_startI <= posI <= op_endI:
        posI = op_endI

    # commands -> 하나씩 하는 게 아니라 다 합해서 하면 됨 -> xx 0초, 마지막초 때문에 안됨. 하나씩 해야함
    for c in commands:
        if c == 'prev':
            if posI < 10:
                posI = 0
            else:
                posI -= 10
        elif c == 'next':
            if posI > video_lenI - 10:
                posI = video_lenI
            else:
                posI += 10
        # 오프닝 건너뛰기 자동 실행
        if op_startI <= posI <= op_endI:
            posI = op_endI

    minute = toStrUnder10(posI // 60)
    second = toStrUnder10(posI % 60)

    answer = minute + ':' + second
    return answer