// Todo: 괄호 짝 맞추기
// return: 가능 여부 boolean

// 1. 괄호문자열 입력받기
// 2. 문자 하나씩 비교
// 2-2. 짝 맞으면 둘 다 제거
// 3. 남은 문자 있는 지 체크해서 가능여부 리턴


function solution(s) {
  const arr = []
  let flag = true
  for (const s1 of s) {
    if (s1 === '(') {
      arr.push(s1)
    } else {
      s2 = arr.pop()
      if (s2 != '(') {
        flag = false
        break
      }
    }
  }

  if (arr.length === 0 && flag) return true
  return false
}

console.log(solution('(())()'));
console.log(solution('((())()'));
