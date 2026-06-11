// 날짜 + n달 째에 파기
// 모든 달은 28일까지 -> 2월 등등 고려x
// 년도는 2000~2022 -> 전부 일로 변환

const strToDay = (date) => {
    const [y, m, d] = date.split('.')
    return (y - 1) * 28 * 12 + (m - 1) * 28 + d * 1
}

function solution(today, terms, privacies) {
    const todayD = strToDay(today)
    const termsMap = {}
    for (const term of terms) {
        const [type, period] = term.split(' ')
        termsMap[type] = period * 28
    }
    
    const ans = []
    for (let i=0; i<privacies.length; i++) {
        const [date, type] = privacies[i].split(' ')
        const dateD = strToDay(date)
        if (dateD + termsMap[type] <= todayD) ans.push(i + 1)
    }
    
    return ans;
}