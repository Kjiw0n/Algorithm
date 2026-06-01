// 테두리가 비어있는 그래프 생성 -> 빈 공간만 지게차가 이동 가능
// 알파벳 하나 - 접근 가능한 컨테이너 (전부)
// - 상하좌우 체크 후 빈 공간 or 테두리 인 경우만 제거
// 알파벳 두개 - 모든 컨테이너

function solution(storage, requests) {
    const n = storage.length
    const m = storage[0].length
    const dx = [-1, 1, 0, 0]
    const dy = [0, 0, -1, 1]
    
    const graph = Array.from({ length: n + 2 }, () => Array(m + 2).fill(''))
    for (let i=1; i<n+1; i++) {
        for (let j=1; j<m+1; j++) {
            graph[i][j] = storage[i - 1][j - 1]
        }
    }
    
    // 지게차 출고 시
    const bfs = (req) => {
        const visited = Array.from({ length: n + 2 }, () => Array(m + 2).fill(false))
        const queue = [[0, 0]]
        visited[0][0] = true
        let head = 0
        
        const arr = []
        
        while (head < queue.length) {
            const [x, y] = queue[head++]
            for (let i=0; i<4; i++) {
                const nx = x + dx[i]
                const ny = y + dy[i]
                if (nx >= 0 && nx < m+2 && ny >= 0 && ny < n+2 && !visited[ny][nx]) {
                    if (graph[ny][nx] === '') queue.push([nx, ny])
                    else if (graph[ny][nx] === req) arr.push([nx, ny])
                    visited[ny][nx] = true
                }
            }
        }
        
        for (const [x, y] of arr) {
            graph[y][x] = ''
        }
    }
    
    const two = (req) => {
        for (let i=1; i<n+1; i++) {
            for (let j=1; j<m+1; j++) {
                if (graph[i][j] === req) graph[i][j] = ''
            }
        }
    }
    
    for (const request of requests) {
        if (request.length === 1) bfs(request)
        else two(request[0])
    }
    
    let ans = 0    
    for (let i=1; i<n+1; i++) {
        for (let j=1; j<m+1; j++) {
            if (graph[i][j] != '') ans++
        }
    }
    
    return ans;
}