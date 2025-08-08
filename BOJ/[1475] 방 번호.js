// [1475] 방 번호

const fs = require("fs");
const str = fs.readFileSync(0, "utf8").trim();

const arr = new Array(10).fill(0);

for (let s of str) {
  s = parseInt(s);
  arr[s]++;
}

// 6이랑 9는 합쳐서 /2
// 그 외 나머지와 해당 값의 max가 답
const arr0_5 = arr.slice(0, 6);
const arr7_8 = arr.slice(7, 9);
const val = Math.ceil((arr[6] + arr[9]) / 2);

const mergeArr = [...arr0_5, ...arr7_8, val];

console.log(Math.max(...mergeArr));
