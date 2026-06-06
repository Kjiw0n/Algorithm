function solution(N, road, K) {
    const graph = Array.from({ length: N + 1 }, () => [])
    for (const [a, b, c] of road) {
        graph[a].push([b, c])
        graph[b].push([a, c])
    }
    
    const dist = Array(N + 1).fill(Infinity)
    dist[1] = 0
    
    const pq = [[1, 0]]
    
    while (pq.length > 0) {
        pq.sort((a, b) => b[1] - a[1])
        const [q, c] = pq.pop()
        
        if (dist[q] < c) continue
        
        for (const [nq, nc] of graph[q]) {
            if (c + nc < dist[nq]) {
                dist[nq] = c + nc
                pq.push([nq, c + nc])
            }
        }
    }
    
    let ans = 0
    for (let i=0; i<N; i++) {
        if (dist[i + 1] <= K) ans++
    }
    
    return ans;
}