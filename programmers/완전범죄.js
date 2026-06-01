// A가 훔치는 경우/B가 훔치는 경우 나눠서 전개 (백트래킹)
// visited 처리 -> 동일 결과 제거 (dp)
// 모든 물건 훔치는 경우 ans에 추가 [A, B]
// ans[][0] 기준으로 오름차순 정렬 후 리턴

function solution(info, n, m) {
    const ans = []
    const visited = new Set()
    
    const dfs = (idx, arr) => {
        if (idx === info.length) {
            ans.push(arr)
            return
        }
        
        const state = `${idx}-${arr[0]}=${arr[1]}`
        if (visited.has(state)) return
        visited.add(state)
        
        if (arr[0] + info[idx][0] < n) {
            dfs(idx + 1, [arr[0] + info[idx][0], arr[1]])            
        }
        if (arr[1] + info[idx][1] < m) {
            dfs(idx + 1, [arr[0], arr[1] + info[idx][1]])
        }
    }
    
    dfs(0, [0, 0])
    
    if (ans.length > 0) {
        ans.sort((a, b) => a[0] - b[0])
        return ans[0][0]
    } else {
        return -1
    }
    
}