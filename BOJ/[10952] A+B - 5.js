let arr = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((i) => i.split(" ").map(Number));

// console.log(...arr);
arr.pop();

for (const a of arr) {
  const sum = a.reduce((acc, cur) => acc + cur, 0);
  console.log(sum);
}
