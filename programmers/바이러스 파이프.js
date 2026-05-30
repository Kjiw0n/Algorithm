// 0. 그래프 만들기
// 1. 파이프 종류 별로 열고 닫기 (백트래킹)
// 1-1. k -= 1
// 2. 열린 파이프 경로 따라 감염

const bfs = (n, edges, cur_type, infected, graph) => {
    const cur_infected = new Set(infected)
    
    const queue = []
    let head = 0
    const visited = Array(n + 1).fill(false)
    
    for (const i of infected) {
        visited[i] = true
        queue.push(i)
    }
    
    while (head < queue.length) {
        const q = queue[head++]
        cur_infected.add(q)
        
        for (const [node, type] of graph[q]) {
            if (!visited[node] && cur_type === type) {
                visited[node] = true
                queue.push(node)
            }
        }
    }
    
    return cur_infected
}

function solution(n, infection, edges, k) {
    const types = [1, 2, 3] // ['A', 'B', 'C']
    
    const graph = Array.from({ length: n + 1 }, () => []);
    for (const [x, y, type] of edges) {
      graph[x].push([y, type]);
      graph[y].push([x, type]);
    }
    
    const infect_set = new Set()
    infect_set.add(infection)
    let max_cnt = 0
    
    const dfs = (K, infected) => {
        if (K === 0 || n === infected.size) {
            max_cnt = Math.max(max_cnt, infected.size)
            return
        }

        for (const type of types) {
            const cur_infected = bfs(n, edges, type, infected, graph)
            dfs(K - 1, cur_infected)
        }
    }
    dfs(k, infect_set)
    
    return max_cnt;
}