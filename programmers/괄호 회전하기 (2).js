// Todo: 왼쪽으로 x칸 만큼 문자열 회전시켜서 올바른 문자열 찾기
// return: 올바른 문자열 만드는 x의 개수

// s의 길이는 1000 이하, 1000개의 문자를 1000번 비교 -> 1000,000 완탐 가능

// 1. s 하나씩 비교
// 1-1. 맨 앞에 -> 맨 뒤로 이동
// 1-2. 올바른 괄호 문자열인 지 비교
// 1-3. 1-1부터 반복
// 2. 올바른 x의 개수 출력

function check(str) {
    const map = {
        '[': ']',
        '{': '}',
        '(': ')'
    }
    const res = []
    for (const s of str) {
        if (s === '[' || s === '(' || s ==='{') {
            res.push(s)
        } else {
            if (res.length === 0) {
                return 0
            }
            const st = res.pop()
            if (map[st] != s) {
                return 0
            }
        }
    }
    return res.length === 0 ? 1 : 0
}

function solution(s) {
    const str = [...s]
    let cnt = 0
    for (let i=0; i<str.length; i++) {
        cnt += check(str)
        const s = str.shift()
        str.push(s)
    }
    
    return cnt;
}