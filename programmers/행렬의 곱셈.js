function solution(arr1, arr2) {
  var answer = [];
  for (let i = 0; i < arr1.length; i++) {
    let r = [];
    for (let k = 0; k < arr2[0].length; k++) {
      let rr = 0;
      for (let j = 0; j < arr2.length; j++) {
        rr += arr1[i][j] * arr2[j][k];
      }
      r.push(rr);
    }

    answer.push(r);
  }
  return answer;
}

// console.log(
//   ...solution(
//     [
//       [1, 4],
//       [3, 2],
//       [4, 1],
//     ],
//     [
//       [3, 3],
//       [3, 3],
//     ]
//   )
// );
