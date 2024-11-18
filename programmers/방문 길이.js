function solution(dirs) {
  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];

  let visit = new Set();
  let i = 5;
  let j = 5;
  let answer = 0;
  let di = 0;
  let dj = 0;
  for (let k = 0; k < dirs.length; k++) {
    di = i + dx[direction(dirs[k])];
    dj = j + dy[direction(dirs[k])];
    if (0 <= di && di < 11 && 0 <= dj && dj < 11) {
      if (!visit.has(`${i},${j},${di},${dj}`)) {
        // js에서 set에 포함되어있는 거 찾기
        answer++;
        // 양방향으로 길 저장
        visit.add(`${i},${j},${di},${dj}`);
        visit.add(`${di},${dj},${i},${j}`);
      }
      i = di;
      j = dj;
    }
  }

  return answer;
}

function direction(d) {
  if (d == "U") {
    return 0;
  } else if (d == "D") {
    return 1;
  } else if (d == "R") {
    return 3;
  } else if (d == "L") {
    return 2;
  }
}
console.log(solution("ULURRDLLU"));
