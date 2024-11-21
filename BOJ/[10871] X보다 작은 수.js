let arr = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((i) => i.split(" ").map(Number));

// console.log(...arr);
const X = arr[0][1];
arr = arr[1];

let answer = [];
for (const a of arr) {
  if (a < X) {
    answer.push(a);
  }
}

console.log(...answer);
