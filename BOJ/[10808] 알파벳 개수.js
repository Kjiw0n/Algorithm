// [10808] 알파벳 개수

const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim();

const arr = new Array(26).fill(0);

let n = 0;
for (const s of input) {
  n = s.charCodeAt() - 97;
  arr[n] += 1;
}

console.log(...arr);
