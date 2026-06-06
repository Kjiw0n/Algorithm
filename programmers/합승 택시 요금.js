// N = 200
// 간선 비용, 양방향
// 특정 지점까지만 같이 가고, 그 후 각자 가기
// s, a, b 각각 최저 경로가 지나는 노드 전부 저장

const dijkstra = (n, s, graph) => {
    const dist = Array(n + 1).fill(Infinity)
    dist[s] = 0
    
    const pq = [[s, 0]]
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
    
    return dist
}

function solution(n, s, a, b, fares) {
    const graph = Array.from({ length: n + 1}, () => [])
    for (const [u, v, c] of fares) {
        graph[u].push([v, c])
        graph[v].push([u, c])
    }
    
    const sDist = dijkstra(n, s, graph)
    const aDist = dijkstra(n, a, graph)
    const bDist = dijkstra(n, b, graph)
    
    let min = Infinity
    for (let i=1; i<n+1; i++) {
        if (min > sDist[i] + aDist[i] + bDist[i]) {
            min = sDist[i] + aDist[i] + bDist[i]
        }
    }
    
    return min;
}