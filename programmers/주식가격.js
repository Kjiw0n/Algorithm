// Todo: 각 초마다 주식 가격이 떨어지지 않은 기간 구하기
// return: 각각 몇 초인 지 배열 리턴

// prices의 길이는 2 이상 100,000 이하 -> N^2까지 가능

// 1. 각 초 별 가격 순회
// 1-2. 순회하면서 유지 시간 저장하기

function solution(prices) {
    const times = []
    for (let i=0; i<prices.length; i++) {
        let time = 0
        let prev = 0
        for (let j=i+1; j<prices.length; j++) {
            time++
            if (prices[j] < prices[i]) break 
        }
        times.push(time)
    }
    
    return times;
}