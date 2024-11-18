def solution(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        r = []
        for k in range(len(arr2[0])):
            rr = 0
            for j in range(len(arr2)):
                rr += arr1[i][j] * arr2[j][k]
                # print('i, j, k', i, j, k, '| a[i][j], b[j][k]', a[i][j], b[j][k], '| rr', rr)
            r.append(rr)
        result.append(r)

    return result
