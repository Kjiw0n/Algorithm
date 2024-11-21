let arr = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

function isAscending(arr) {
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] != arr[i - 1] + 1) {
      // 이전 항보다 1 오른 수가 아니라면
      return false;
    }
  }

  return true;
}

function isDescending(arr) {
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] != arr[i - 1] - 1) {
      // 이전 항보다 1 적은 수가 아니라면
      return false;
    }
  }

  return true;
}

if (isAscending(arr)) {
  console.log("ascending");
} else if (isDescending(arr)) {
  console.log("descending");
} else {
  console.log("mixed");
}
