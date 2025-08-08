// [2576] 홀수

const fs = require("fs");
const arr = fs.readFileSync(0, "utf8").trim().split("\n").map(Number);

let total = 0;
let min = 100;
for (a of arr) {
  if (a % 2 == 0) continue;
  total += a;
  min = min > a ? a : min;
}

if (total === 0) {
  console.log(-1);
  return;
}

console.log(total);
console.log(min);
