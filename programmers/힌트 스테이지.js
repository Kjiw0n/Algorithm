// 백트래킹 - 힌트 사는 경우, 안사는 경우
// i번 힌트권은 i번 스테이지에서만 사용 가능

function solution(cost, hint) {
    const n = cost.length
    
    const hints = Array(n).fill(0) // hints[i]: i번 힌트권 개수
    
    let min_total = Infinity
    const game = (total, idx) => {
        if (idx >= n) {
            min_total = Math.min(min_total, total)
            return
        }
        
        const hint_num = Math.min(cost[idx].length - 1, hints[idx])
        total += cost[idx][hint_num]
        game(total, idx + 1)
        
        if (idx < n - 1) {
            for (let i=1; i<hint[idx].length; i++) {
                hints[hint[idx][i] - 1]++
            }
            game(total + hint[idx][0], idx + 1)
            for (let i=1; i<hint[idx].length; i++) {
                hints[hint[idx][i] - 1]--
            }
        }   
    }
    
    
    game(0, 0)
    return min_total;
}