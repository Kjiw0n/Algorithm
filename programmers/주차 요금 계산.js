// N = 10^3, M(:시간) = 24*60

// 입/출차 기록을 key가 차량 번호인 map으로 정리 후 계산

// 분 단위 변환
const strToTime = (str) => {
    const arr = str.split(':')
    return arr[0] * 60 + arr[1] * 1
}

function solution(fees, records) {
    const [basicTime, basicFee, eachTime, eachFee] = fees
    const map = {}
    
    for (const record of records) {
        const [time, car, inout] = record.split(' ')
        
        if (inout === 'IN') {
            (map[car] ??= []).push([0, 23*60+59])
            map[car].at(-1)[0] = strToTime(time)
        }
        else map[car].at(-1)[1] = strToTime(time)
    }
    
    const arr = [] // 차량 번호, 요금
    for (const car of Object.keys(map)) {
        let sum = 0
        for (const [inT, outT] of map[car]) {
            sum += outT - inT
        }
        let cost = basicFee
        sum -= basicTime
        sum /= eachTime
        cost += sum > 0 ? Math.ceil(sum) * eachFee : 0
        arr.push([car, cost])
    }
    
    arr.sort((a, b) => a[0] - b[0])
    const ans = []
    for (const [_, fee] of arr) ans.push(fee)
    
    return ans;
}