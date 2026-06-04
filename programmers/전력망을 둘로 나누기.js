function solution(n, wires) {
    let minAns = n
    for (let i=0; i<wires.length; i++) {
        const graph = Array.from({ length: n + 1 }, () => [])
        
        for (j=0; j<wires.length; j++) {
            if (j === i) continue
            
            graph[wires[j][1]].push(wires[j][0])
            graph[wires[j][0]].push(wires[j][1])
        }
        
        const bfs = (s) => {
            const queue = [s]
            let head = 0
            const visited = Array(n + 1).fill(false)
            visited[s] = true
            
            let cnt = 0
            while (head < queue.length) {
                const q = queue[head++]
                cnt++
                
                for (const nq of graph[q]) {
                    if (!visited[nq]) {
                        queue.push(nq)
                        visited[nq] = true
                    }
                }
            }
            return cnt
        }
        
        // 전체 - (1번 wire와 연결되어있는 wire개수)
        const a = bfs(1)
        const b = n - a
        minAns = Math.min(minAns, Math.abs(a - b))
    }
    
    return minAns;
}