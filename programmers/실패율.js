function solution(N, stages) {
  var answer = Array(N).fill(0);

  // 배열 내림차순 정렬 -> 맨 뒤부터 비교 후 pop
  stages.sort((a, b) => a - b);

  let currentN = 1;
  let currentP = 0;
  // 적게 도달한 스테이지부터 빼자. stages 존재할때까지 O(N)
  while (currentN <= N) {
    let currentLen = stages.length;

    while (stages.length != 0) {
      // 해당 스테이지에 머물고 있는 사람 몇명인지 O(len(stages))
      if (stages[0] > currentN) {
        // 해당 스테이지 없는 경우
        break;
      }

      const s = stages.shift();
      if (s == currentN) {
        currentP++;
      }
    }

    answer[currentN - 1] = currentP / currentLen;
    currentN++;
    currentP = 0;
  }

  // let result = [];

  // 비율 큰 순서대로 인덱스 출력 O(N)

  return answer
    .map((value, index) => ({ value, index })) // 값과 인덱스를 객체로 저장
    .sort((a, b) => b.value - a.value) // 내림차순 정렬
    .map((item) => item.index + 1);
}

console.log("solution", ...solution(5, [2, 1, 2, 6, 2, 4, 3, 3]));
console.log("-----");
console.log("solution", ...solution(4, [4, 4, 4, 4, 4]));

// 최악의 경우 O(N^2)
