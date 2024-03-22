def solution(array, commands):
    answer = []
    for c in commands:
        temp = []
        temp = array[c[0] - 1:c[1]]
        temp.sort()
        print(temp)
        answer.append(temp[c[2] - 1])

    return answer