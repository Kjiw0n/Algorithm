// [10804] 카드 역배치

const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");

const arr = Array.from({ length: 20 }, (_, i) => i + 1);
for (line of input) {
  const [s, e] = line.split(" ").map(Number);

  for (let i = s - 1, j = e - 1; i < e, j >= s; i++, j--) {
    if (i >= j) break;
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
}

console.log(arr.join(" "));
