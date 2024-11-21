let arr = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim()
  .split(" ");

arr = arr.map((a) => Number(a));

if (arr[1] >= 45) {
  arr[1] -= 45;
} else {
  if (arr[0] >= 1) {
    arr[0] -= 1;
  } else {
    arr[0] += 24 - 1;
  }
  arr[1] += 60 - 45;
}

console.log(arr[0], arr[1]);
