function solution(maps) {
    const dx = [-1, 1, 0, 0]
    const dy = [0, 0, -1, 1]
    const N = maps.length
    const M = maps[0].length
    
    const visited = Array.from({ length: N }, () => Array(M).fill(false))
    
    const bfs = (sx, sy) => {
        const queue = [[sx, sy]]
        visited[sy][sx] = true
        let head = 0
        let cnt = 0
        
        while (head < queue.length) {
            const [x, y] = queue[head++]
            cnt += (maps[y][x] * 1)
            
            for (let d=0; d<4; d++) {
                const nx = x + dx[d]
                const ny = y + dy[d]
                if (nx >= 0 && nx < M && ny >= 0 && ny < N && !visited[ny][nx] && maps[ny][nx] != 'X') {
                    queue.push([nx, ny])
                    visited[ny][nx] = true
                }
            }
        }
        return cnt
    }
    
    let ans = []
    for (let y=0; y<N; y++) {
        for (let x=0; x<M; x++) {
            if (!visited[y][x] && maps[y][x] !== 'X') {
                ans.push(bfs(x, y))
            }
        }
    }
    
    ans.sort((a, b) => a - b)
    return ans.length > 0 ? ans : [-1];
}