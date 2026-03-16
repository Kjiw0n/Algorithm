// Todo: 입력값 10진수 -> 2진수 변환
// return: 변환된 2진수 값

// 1. 입력된 10진수 값을 2로 계속 나누기
// 1-1. 나머지 저장
// 1-2. 몫(정수)이 0이 될 때까지 나누기
// 2. 변환된 2진수 값 리턴

function solution(num) {
  const arr = []
  
  while (num / 2 != 0) {
    arr.push(num % 2)
    num = Math.floor(num / 2)
  }

  arr.reverse()
  return arr.join('')
}

console.log(solution(10));
console.log(solution(27));
console.log(solution(12345));