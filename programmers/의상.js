// 하루에 최소 한 개의 의상만 입으면 됨

// 1. 각 종류 별 빈 값 추가
// 2. 각 종류별로 하나씩 고르는 경우의 수 찾기, 아무것도 안입는 경우만 제외

function solution(clothes) {
    const dict = {}
    
    for (const [name, type] of clothes) {
        (dict[type] ??= []).push(name)
    }
    
    let ans = 1
    for (const arr of Object.values(dict)) {
        ans *= arr.length + 1
    }
    
    return ans - 1;
}