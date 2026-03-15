// Todo: 처음 걸어본 길의 길이 구하기
// return: 처음 걸어본 길의 길이

// 1. 초기세팅
// 1-1. 좌표평면 그리기
// 1-2. 게임 캐릭터 세우기
// 2. 게임 캐릭터 움직이기
// 2-1. 상하좌우 명령어대로 이동
// 2-2. 각 점의 방향을 저장
// 3. 중복 방향 제거 -> 길 개수 카운트

// 주의: 위로 가는 것과 밑으로 가는 길이 같다면, 그 중복도 제거해야함. @@@@

const switchDirToIdx = (dir) => {
    if (dir === 'U') return 0
    else if (dir === 'D') return 1
    else if (dir === 'R') return 2
    else return 3
}

function solution(dirs) {
    let x = 5, y = 5
    
    const dx = [0, 0, 1, -1]
    const dy = [-1, 1, 0, 0]
    
    const record = new Set()
    for (const dir of dirs) {
        const idx = switchDirToIdx(dir)
        const nx = x + dx[idx], ny = y + dy[idx]
        if (nx >= 0 && nx <= 10 && ny >= 0 && ny <= 10) {
            record.add(`${x}, ${y}, ${nx}, ${ny}`)
            record.add(`${nx}, ${ny}, ${x}, ${y}`)
            x = nx, y = ny   
        }
    }
    
    return record.size / 2
}