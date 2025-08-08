const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim().split("\n");

const [N, X] = input[0].split(" ").map(Number);
const arr = input[1].split(" ").map(Number);

console.log(...arr.filter((x) => x < X));
