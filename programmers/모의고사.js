function solution(answers) {
  const n = answers.length;
  const p1 = [1, 2, 3, 4, 5];
  const p2 = [2, 1, 2, 3, 2, 4, 2, 5];
  const p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  const pattern = [p1, p2, p3];

  const arr = [];

  for (const p of pattern) {
    let N = n;
    let a = [];
    if (N >= p.length) {
      for (let i = 0; i < Math.floor(N / p.length); i++) {
        a.push(...p);
      }
      N %= p.length;
    }

    a.push(...p.slice(0, N));
    arr.push(a);
  }

  let cnt = [0, 0, 0];
  for (let j = 0; j < 3; j++) {
    for (let i = 0; i < n; i++) {
      if (answers[i] == arr[j][i]) {
        cnt[j]++;
      }
    }
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
