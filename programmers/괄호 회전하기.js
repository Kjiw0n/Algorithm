function solution(s) {
  // 0 <= x < s.length
  arr = s.split("");

  let answer = 0;
  for (let i = 0; i < s.length; i++) {
    let a = arr.shift();
    arr.push(a);
    if (isTrue(arr)) {
      answer++;
    }
  }

  return answer;
}

console.log(solution("[](){}"));
console.log(solution("}]()[{"));
console.log(solution("[)(]"));
console.log(solution("}}}"));

function isTrue(str) {
  let open = [];
  for (let i = 0; i < str.length; i++) {
    if (str[i] == "(" || str[i] == "{" || str[i] == "[") {
      open.push(str[i]);
    } else {
      if (open.length == 0) {
        return false;
      }

      let o = open.pop();

      if (
        (str[i] == ")" && o != "(") ||
        (str[i] == "}" && o != "{") ||
        (str[i] == "]" && o != "[")
      ) {
        return false;
      }
    }
  }
  return open.length == 0;
}
