let arr = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

let answer = new Set();
for (const a of arr) {
  answer.add(a % 42);
}

console.log(answer.size);
