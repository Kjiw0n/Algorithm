let score = Number(require("fs").readFileSync(
    process.platform === "linux" ? "/dev/stdin" : "input.txt")
);

if (score >= 90 && score <= 100) {
    console.log('A');
} else if (score >= 80 && score < 90) {
    console.log('B');
} else if (score >= 70 && score < 80) {
    console.log('C');
} else if (score >= 60 && score < 70) {
    console.log('D');
} else {
    console.log('F');
}
