// [5397] 키로거

const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");

const ans = [];
const len = parseInt(input[0]);
for (let i = 1; i < len + 1; i++) {
  const str = input[i].split("");

  const left = [];
  const right = [];
  for (let j = 0; j < str.length; j++) {
    switch (str[j]) {
      case "-":
        if (left.length === 0) break;
        left.pop();
        break;
      case "<":
        if (left.length === 0) break;
        right.push(left.pop());
        break;
      case ">":
        if (right.length === 0) break;
        left.push(right.pop());
        break;
      default:
        left.push(str[j]);
        break;
    }
  }
  ans.push(left.concat(right.reverse()).join(""));
}

console.log(ans.join("\n"));
