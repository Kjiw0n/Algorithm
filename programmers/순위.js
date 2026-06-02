// N = 100, M = 4500

function solution(n, results) {
    const win = Array.from({ length: n + 1 }, () => [])
    const lose = Array.from({ length: n + 1 }, () => [])
    for (const [a, b] of results) {
        win[a].push(b)
        lose[b].push(a)
    }
    
    const bfs = (s, arr) => {
        const queue = [s]
        let head = 0
        const visited = Array(n + 1).fill(false)
        visited[s] = true
        
        let cnt = -1
        while (head < queue.length) {
            const q = queue[head++]
            cnt++
            for (const nq of arr[q]) {
                if (!visited[nq]) {
                    queue.push(nq)
                    visited[nq] = true
                }
            }
        }
        return cnt
    }
    
    let ans = 0
    for (let i=1; i<n+1; i++) {
        if (bfs(i, win) + bfs(i, lose) === n - 1) ans++
    }
    return ans;
}