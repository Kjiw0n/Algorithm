// 1. name-yearning을 매핑해서 저장한다.
// 2. 각 photo의 사람들을 한명씩 1번 맵을 조회하며 점수 저장
// 3. 각 photo의 점수 출력

// 100 * 100, N = photo <= 100, O(N^2)

function solution(name, yearning, photo) {
    let map = {}
    for (let i=0; i<name.length; i++) {
        map[name[i]] = yearning[i]
    }
    
    let ans = []
    for (const photoItem of photo) {
        let n = 0
        for (const name of photoItem) {
            if (map[name] === undefined) continue
            n += map[name]
        }
        ans.push(n)
    }
    
    return ans;
}