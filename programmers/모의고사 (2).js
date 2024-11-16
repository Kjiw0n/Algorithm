function solution(answers) {
  const p1 = [1, 2, 3, 4, 5];
  const p2 = [2, 1, 2, 3, 2, 4, 2, 5];
  const p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  const pattern = [p1, p2, p3];

  let cnt = [];
  for (const p of pattern) {
    let c = 0;
    for (let i = 0; i < answers.length; i++) {
      if (answers[i] == p[i % p.length]) {
        c++;
      }
    }
    cnt.push(c);
  }

  M = Math.max(...cnt);
  var answer = [];
  for (let i = 0; i < cnt.length; i++) {
    if (cnt[i] == M) {
      answer.push(i + 1);
    }
  }

  return answer;
}
