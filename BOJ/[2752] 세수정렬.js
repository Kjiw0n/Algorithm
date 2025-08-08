const fs = require("fs");

const arr = fs.readFileSync(0, "utf8").trim().split(" ").map(Number);
arr.sort((a, b) => a - b);
console.log(arr.join(" "));
