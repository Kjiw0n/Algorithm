let n = Number(
  require("fs").readFileSync(
    process.platform === "linux" ? "/dev/stdin" : "input.txt"
  )
);

let x = 0, y = 1;

for (let i = 0; i < n; i++) {
  [x, y] = [y, x + y];
}

console.log(x);
