// [2587] 대표값2

const fs = require("fs");
const arr = fs.readFileSync(0, "utf8").trim().split("\n").map(Number);

arr.sort((a, b) => a - b);
const avg = arr.reduce((a, b) => a + b) / 5;
const mid = arr[2];

console.log(avg + "\n" + mid);
