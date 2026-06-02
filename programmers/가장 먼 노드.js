// n = 2*10^4

function solution(n, edge) {
    const graph = Array.from({ length: n + 1 }, () => [])
    for (const [s, e] of edge) {
        graph[s].push(e)
        graph[e].push(s)
    }
    
    const queue = [[1, 0]]
    let head = 0
    const visited = Array(n + 1).fill(false)
    visited[1] = true
    
    while (head < queue.length) {
        const [q, dist] = queue[head++]
        
        for (const nq of graph[q]) {
            if (!visited[nq]) {
                queue.push([nq, dist + 1])
                visited[nq] = true
            }
        }
    }
    
    queue.sort((a, b) => b[1] - a[1])    
    const max_dist = queue[0][1]
    let cnt = 0
    for (let i=0; i<queue.length; i++) {
        if (max_dist === queue[i][1]) cnt++
        else break
    }
    
    return cnt;
}