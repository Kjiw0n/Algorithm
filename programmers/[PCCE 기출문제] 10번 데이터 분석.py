# Todo: 조건에 맞게 데이터 필터링 후, 정렬 기준에 따라 오름차순 정렬
# return: 필터링 후 정렬된 데이터 리턴

# 1. 데이터 필터링 (ext항목이 val_ext보다 작은 경우)
# 2. 필터링된 데이터 정렬

# 시간복잡도 N:data길이(=500), O(N)

def solution(data, ext, val_ext, sort_by):
    idxMap = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    
    filterIdx = idxMap[ext]
    arr = []
    for d in data:
        if d[filterIdx] < val_ext:
            arr.append(d)
    
    sortIdx = idxMap[sort_by]
    arr.sort(key=lambda x: x[sortIdx])
    
    return arr