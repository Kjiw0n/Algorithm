// [1158] 요세푸스 문제

const fs = require("fs");
const [N, K] = fs.readFileSync(0, "utf8").trim().split(" ").map(Number);

const queue = Array.from({ length: N }, (_, i) => i + 1);
const ans = [];

while (queue.length > 0) {
  for (let i = 0; i < K - 1; i++) {
    queue.push(queue.shift());
  }

  ans.push(queue.shift());
}

console.log(`<${ans.join(", ")}>`);
