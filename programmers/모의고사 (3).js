function solution(answers) {
    // 1번은 1, 2, 3, 4, 5 반복
    // 2번은 2, 1, 2, 2, 2, 3, 2, 4, 2, 5 반복 (2, i)
    // 3번은 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 반복
    
    // N = 10,000 -> 완탐 가능함. (전체 for문 돌려도 N * 3)
    // 누가 가장 많이 맞췄는 지 찾기
    // 1. 개별 정답 체크
    // 1-1. 1, 2, 3번의 각각 반복 규칙 찾기
    // 1-2. 정답 배열과 비교
    // 2. 맞춘 개수 비교
    
    const ans1 = [1, 2, 3, 4, 5]
    const ans2 = [2, 1, 2, 3, 2, 4, 2, 5]
    const ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    const ans = [ans1, ans2, ans3]
    
    const cntArr = [0, 0, 0]
    
    for(let t=0; t<3; t++) {
        const each = ans[t]
        const len = each.length
        for(let i=0; i<answers.length; i++) {
            const idx = i % len
            if (answers[i] === each[idx]) {
                cntArr[t]++;
            }
        }
    }
    
    const result = []
    
    const maxCnt = Math.max(...cntArr)
    for(let i=0; i<3; i++) {
        if (maxCnt === cntArr[i])
            result.push(i + 1)
    }
    
    return result
}