// [17298] 오큰수

const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");
const N = parseInt(input[0]);
const arr = input[1].split(" ").map(Number);

const ans = new Array(N).fill(-1);
const stack = [];
for (let i = 0; i < N; i++) {
  if (stack.length === 0) {
    stack.push(i);
    continue;
  }
  while (arr[i] > arr[stack[stack.length - 1]]) {
    ans[stack.pop()] = arr[i];
  }
  stack.push(i);
}

console.log(ans.join(" "));
