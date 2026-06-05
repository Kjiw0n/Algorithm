// N(: 판매원 수) = 10^4, M(: 판매 건 수) = 10^5

// 각 판매원의 이익금 리턴
// 이익금 = 칫솔 판매액 * 0.9 + (자식들의 이익 * 0.1)
// 자식들의 이익은 루트까지 올라감
// 이 때, root로 가는 금액은 전부 버려짐

function solution(enroll, referral, seller, amount) {
    const graph = {} // 이름: 추천해준 사람
    const add = {} // 이름: 이익금
    for (let i=0; i<enroll.length; i++) {
        graph[enroll[i]] = referral[i]
        add[enroll[i]] = 0
        totalSell[enroll[i]] = 0
    }
    
    for (let i=0; i<seller.length; i++) {
        let rest = amount[i] * 100
        let p = seller[i]
        while (p !== '-') {
            if (rest * 0.1 < 1) {
                add[p] += rest
                break
            } else {
                add[p] += (rest - Math.floor(rest * 0.1))
                rest = Math.floor(rest * 0.1)
            }
            p = graph[p]
        }
    }
    
    const ans = []
    for (const name of enroll) {
        ans.push(add[name])
    }
    
    return ans;
}