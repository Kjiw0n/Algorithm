// [15552] 빠른 A+B

const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split(/\s+/).map(Number);
const len = input[0];

let result = "";
for (let i = 1; i < len * 2; i += 2) {
  result += input[i] + input[i + 1] + "\n";
}

process.stdout.write(result);
