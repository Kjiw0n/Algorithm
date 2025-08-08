const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split("\n");

const result = ["D", "C", "B", "A", "E"];
for (line of input) {
  const arr = line.split(" ").map(Number);
  const total = arr.reduce((a, b) => a + b);
  console.log(result[total]);
}
