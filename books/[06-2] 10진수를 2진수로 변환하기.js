function solution(num) {
  let n = 2;

  let stack = [];
  while (num >= 1) {
    stack.push(num % 2);
    if (num / 2 != 0) {
      num = Math.floor(num / 2);
    }
  }

  stack.reverse();
  console.log(stack);
  let answer = stack.join("");
  return answer;
}

console.log(solution(12345));
