// [2577] 숫자의 개수

const fs = require("fs");
const arr = fs.readFileSync(0, "utf8").trim().split("\n").map(Number);

const tot = String(arr[0] * arr[1] * arr[2]);
const ans = new Array(10).fill(0);

for (let t of tot) {
  t = parseInt(t);
  ans[t]++;
}

console.log(ans.join("\n"));
