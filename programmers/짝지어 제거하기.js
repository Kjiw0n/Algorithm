// Todo: 주어진 문자열에서 같은 알파벳 2개 붙어있는 짝 찾아서 제거하기
// return: 주어진 문자열 전부 제거 시 0, 아니면 1

// 문자열의 길이 : 1,000,000이하 -> 중첩 안됨. 한번만 돌 수 있음
// 괄호로 생각하면?

// 1. 주어진 문자열 한 문자 씩 비교
// 1-1. 한 문자 씩 저장 (res)
// 1-2. res의 가장 마지막 문자와 같으면 마지막 문자 제거, 다르면 새로운 문자 추가
// 1-3. res가 다 없어질 때까지 계속 비교? 
// 1-4. 비교 중에, 제거된 문자가 아무것도 없다면 비교 종료
// 1-5. 전부 제거 성공 시 1, 아니면 0 리턴

function solution(str) {
    const res = []
    let prev = ''
    for (const s of str) {
        if (s == prev) {
            res.pop()
            prev = res.at(-1)
        } else {
            res.push(s)
            prev = s
        }
    }
    
    return res.length === 0 ? 1 : 0;
}