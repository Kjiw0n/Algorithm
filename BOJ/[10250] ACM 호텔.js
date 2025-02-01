let arr = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((i) => i.split(" ").map(Number));

// console.log("arr", ...arr);

for (let i = 1; i <= arr[0]; i++) {
  const H = arr[i][0];
  const W = arr[i][1];
  const N = arr[i][2];

  room = [N % H, Math.floor(N / H) + 1];

  if (room[0] == 0) {
    room[0] = H;
    room[1]--;
  }

  console.log(`${room[0]}${String(room[1]).padStart(2, "0")}`);
}
