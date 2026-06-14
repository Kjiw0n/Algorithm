// N = 50
// 5개씩 묶음, 점수 내림차순 정렬

function solution(picks, minerals) {
    const picksArr = [...Array(picks[0]).fill('diamond'), ...Array(picks[1]).fill('iron'), ...Array(picks[2]).fill('stone')]
    let head = 0
    
    const map = {}
    map['diamond'] = {
        'diamond': 1,
        'iron': 1,
        'stone': 1
    }
    map['iron'] = {
        'diamond': 5,
        'iron': 1,
        'stone': 1
    }
    map['stone'] = {
        'diamond': 25,
        'iron': 5,
        'stone': 1
    }
    
    const sumPicks = picks.reduce((acc, cur) => acc + cur)
    const maxMenerals = sumPicks * 5
    const mineralsLen = Math.min(maxMenerals, minerals.length)
    
    const arr = []
    let chunk = []
    let score = 0
    
    for (let i=0; i<mineralsLen; i++) {
        chunk.push(minerals[i])
        if (minerals[i] === 'diamond') score += 25
        if (minerals[i] === 'iron') score += 5
        else score += 1
        if ((i + 1) % 5 === 0 || i === mineralsLen - 1) {
            arr.push([chunk, score])
            chunk = []
            score = 0
        }
    }
    
    arr.sort((a, b) => b[1] - a[1])
    
    let ans = 0
    for (const [chunk, _] of arr) {
        const pick = picksArr[head++]
        for (const c of chunk) {
            ans += map[pick][c]
        }
    }
    
    return ans;
}