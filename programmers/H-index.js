// N = 10^3, M = 10^5 -> NM = 10^8, 완탐x

// 인용 횟수(citations) 정렬
// h = n - i
// h번 이상 인용된 논문이 h편 이상, 나머지
// citatinos[i]번 이상 인용된 논문이 (n - i)편 이상

function solution(citations) {
    citations.sort((a, b) => a - b)
    
    const n = citations.length
    let ans = 0
    for (let i=0; i<n; i++) {
        if (citations[i] >= n - i) {
            ans = n - i
            break
        }
    }
    
    return ans;
}