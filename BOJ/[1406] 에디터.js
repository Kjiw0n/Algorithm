// [1406] 에디터

const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");

const str = input[0];
const M = parseInt(input[1]);

const left = str.split("");
const right = [];

for (let i = 2; i < M + 2; i++) {
  const command = input[i].split(" ");

  switch (command[0]) {
    case "L":
      if (left.length === 0) break;
      right.push(left.pop());
      break;
    case "D":
      if (right.length === 0) break;
      left.push(right.pop());
      break;
    case "B":
      if (left.length === 0) break;
      left.pop();
      break;
    case "P":
      left.push(command[1]);
      break;
  }
}

const ans = left.concat(right.reverse());

console.log(ans.join(""));
