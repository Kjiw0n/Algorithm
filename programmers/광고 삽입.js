// N = 3*10^5, M(:시간) = 99*60*60 = 36*10^4

// 가장 많이 보는 구간(연속 구간)에 광고넣기
// 광고 길이: 윈도우 길이
// 시간은 전부 초 기준으로 바꾸기

const strToTime = (str) => {
    str = str.split(':')
    return str[0] * 60 * 60 + str[1] * 60 + str[2] * 1
}

const timeToStr = (time) => {
    let s = time % 60
    let h = Math.floor(time / 60 / 60)
    let m = Math.floor(time / 60) % 60
    
    if (h < 10) h = '0' + h
    if (m < 10) m = '0' + m
    if (s < 10) s = '0' + s
    return h + ':' + m + ':' + s
}

function solution(play_time, adv_time, logs) {
    const playTime = strToTime(play_time)
    const advTime = strToTime(adv_time)
    
    const times = Array(playTime + 1).fill(0)
    for (let i=0; i<logs.length; i++) {
        const arr = logs[i].split('-')
        times[strToTime(arr[0])]++
        times[strToTime(arr[1])]--
    }
    
    for (let i=1; i<playTime + 1; i++) {
        times[i] += times[i - 1]
    }
    
    let ans = 0 // 광고 시작 시간
    let sum = 0 // 현재 누적 재생 시간
    let max = 0 // 최대 누적 재생 시간
    
    for (let i=0; i<advTime; i++) {
        sum += times[i]
    }
    max = sum
    for (let i=advTime; i<playTime + 1; i++) {
        sum -= times[i - advTime]
        sum += times[i]
        
        if (max < sum) {
            max = sum
            ans = i - advTime + 1
        }
    }
    
    return timeToStr(ans);
}