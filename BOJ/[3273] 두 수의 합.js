// [3273] 두 수의 합

const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");

const n = parseInt(input[0]);
const arr = input[1].split(" ").map(Number);
const x = parseInt(input[2]);

arr.sort((a, b) => a - b);

let i = 0,
  j = n - 1,
  cnt = 0;

while (i < j) {
  const s = arr[i] + arr[j];
  if (s === x) {
    cnt++;
    i++;
    j--;
  } else if (s > x) j--;
  else i++;
}

console.log(cnt);
