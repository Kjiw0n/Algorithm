let arr = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim()
  .split("\n");

console.log(Number(arr[0]) + Number(arr[1]) - Number(arr[2]));
console.log(arr[0] + arr[1] - arr[2]);
