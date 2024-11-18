function solution(N, stages) {
  const fails = {};

  const challenger = Array(N + 2).fill(0); // O(n)
  for (const s of stages) {
    // O(len(stages) = m)
    challenger[s]++;
  }

  let total = stages.length;
  for (let i = 1; i <= N; i++) {
    // O(n)
    if (challenger[i] === 0) {
      fails[i] = 0;
    }

    fails[i] = challenger[i] / total;
    total -= challenger[i];
  }

  const result = Object.entries(fails).sort((a, b) => b[1] - a[1]); // Object.entries(fails): O(n) + sort: O(n logn)
  return result.map((v) => Number(v[0])); // O(n)
}

console.log("solution", ...solution(5, [2, 1, 2, 6, 2, 4, 3, 3]));
console.log("-----");
console.log("solution", ...solution(4, [4, 4, 4, 4, 4]));

// O(M + NlogN)
