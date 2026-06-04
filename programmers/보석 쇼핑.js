// N = 10^5, 2중for문 안됨
// 보석 종류 전부 포함하는 가장 짧은 구간 -> 슬라이딩윈도우/투포인터

function solution(gems) {
    const N = (new Set(gems)).size
    
    const cur = {}
    let cnt = 0
    
    let min = gems.length + 1
    let ans = []
    
    let head = 1
    for (let rear=1; rear<gems.length + 1; rear++) {
        if (!cur[gems[rear - 1]]) {
            cur[gems[rear - 1]] = 0
            cnt++
        }
        cur[gems[rear - 1]]++
        
        while (cnt === N) {
            if (min > rear - head + 1) {
                ans = [head, rear]
                min = rear - head + 1
            }
            
            cur[gems[head - 1]]--
            if (cur[gems[head - 1]] === 0) {
                cnt--
                delete cur[gems[head - 1]]
            }
            head++
        }        
    }
    
    return ans;
}