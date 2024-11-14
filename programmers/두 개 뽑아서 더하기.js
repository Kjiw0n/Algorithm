function solution(numbers) {
  // for문 돌려서 a[i]랑 a[j] 더한 값 다 저장한 후, Set 먹이고 sort 하면 된다.
  // 이렇게 해도 시간복잡도는 O(n^2)

  let arr = [];

  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      arr.push(numbers[i] + numbers[j]);
    }
  }

  var answer = [...new Set(arr)];
  answer.sort((a, b) => a - b);
  return answer;
}
