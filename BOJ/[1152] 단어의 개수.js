let sentence = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim();

console.log(sentence === "" ? 0 : sentence.split(/\s+/).length);
