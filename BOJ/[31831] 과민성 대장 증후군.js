let input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim()
  .split("\n");


const [N, M] = input[0].split(" ").map(Number);
const arr = input[1].split(" ").map(Number);

let cnt = 0;
let result = 0;

for (const a of arr) {
    if (cnt + a >= 0) {
        cnt += a;
    } else {
        cnt = 0;
    }
    if (cnt >= M) {
        result += 1;
    }
}

console.log(result);