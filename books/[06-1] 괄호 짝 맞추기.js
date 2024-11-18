function solution(str) {
  let open = [];
  str = str.split("");
  console.log(str);

  for (let i = 0; i < str.length; i++) {
    // O(n)
    if ("(" == str[i]) {
      open.push(i);
    }
  }
  // open이 아니면 close겠지
  let answer = true;
  // 맨 마지막 open 바로 뒤에 )가 있어야 하는거
  while (open.length != 0) {
    // while: O(n), splice: O(n^2) -> O(n^2)
    let o = open.pop();
    console.log("str, str[o], o", str, str[o], o);
    if (o == str.length - 1) {
      // ( 뒤에 아무것도 없다 => 바로 false 리턴
      return false;
    }

    if (str[o + 1] == ")") {
      str.splice(o + 1, 1);
      str.splice(o, 1);
      continue;
    }
  }

  return answer;
}

console.log(solution("((())()"));
console.log(solution("(())()"));

// O(n^2)

// 개선. 전체 O(n)
function solution1(str) {
  let openCnt = 0;

  for (let i = 0; i < str.length; i++) {
    if (str[i] == "(") {
      openCnt++;
    } else if (str[i] == ")") {
      if (openCnt == 0) {
        return false;
      }
      // 열린 괄호 앞에 있었으면
      openCnt--;
    }
  }

  // 모든 괄호 짝지어짐
  return openCnt == 0;
}
