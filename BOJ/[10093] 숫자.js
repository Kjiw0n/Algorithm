// [10093] 숫자

const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split(" ").map(Number);

input.sort((a, b) => a - b);
let ans = [];
for (let i = input[0] + 1; i < input[1]; i++) {
  ans.push(i);
}

process.stdout.write(ans.length + "\n" + ans.join(" "));
