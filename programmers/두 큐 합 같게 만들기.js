// N = 3*10^5, M = 10^9

// 각 큐의 원소 합이 같도록
// 목표값(: 전체 합의 /2)부터 찾기
// q1 -> q2, q2 -> q1 각각 해보고 더 작은 횟수 리턴, 둘 다 안되면 -1

function solution(queue1, queue2) {
    const sum1 = queue1.reduce((acc, cur) => acc + cur)
    const sum2 = queue2.reduce((acc, cur) => acc + cur)
    const goal = (sum1 + sum2) / 2
    if (goal !== Math.floor(goal)) return -1 // 큐는 정수배열
    
    const maxCnt = (queue1.length + queue2.length) * 2 // 각 한바퀴씩 돌았으면 충분함
    
    let cnt = 0
    let sumQ1 = sum1
    let sumQ2 = sum2
    let head1 = 0
    let head2 = 0
    while (head1 < queue1.length && head2 < queue2.length && sumQ1 !== sumQ2 && cnt <= maxCnt) {
        if (sumQ1 > sumQ2) {
            const q = queue1[head1++]
            sumQ1 -= q
            sumQ2 += q
            queue2.push(q)
        } else {
            const q = queue2[head2++]
            sumQ1 += q
            sumQ2 -= q
            queue1.push(q)
        }
        cnt++
    }
    
    if (sumQ1 === sumQ2) return cnt
    return -1;
}