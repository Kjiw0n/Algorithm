// 250000 * 1000 * 1000 = 250,000,000,000 -> 완탐 불가, dp

function solution(board, skill) {
    const N = board.length
    const M = board[0].length
    
    const dp = Array.from({ length: N + 1 }, () => Array(M + 1).fill(0))
    
    for (const sk of skill) {
        const [type, r1, c1, r2, c2, degree] = sk
        const deg = type === 1 ? -degree : degree
        
        dp[r1][c1] += deg
        dp[r1][c2 + 1] -= deg
        dp[r2 + 1][c1] -= deg
        dp[r2 + 1][c2 + 1] += deg
    }
    
    for (let y=0; y<N; y++) {
        for (let x=1; x<M; x++) {
            dp[y][x] += dp[y][x-1]
        }
    }
    
    for (let x=0; x<M; x++) {
        for (let y=1; y<N; y++) {
            dp[y][x] += dp[y-1][x]
        }
    }
    
    let cnt = 0
    for (let y=0; y<N; y++) {
        for (let x=0; x<M; x++) {
            if (board[y][x] + dp[y][x] > 0) cnt++
        }
    }
    
    return cnt;
}