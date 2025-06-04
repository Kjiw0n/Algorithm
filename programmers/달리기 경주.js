function solution(players, callings) {
  // splice, indexOf -> 시간초과

  // let name = '';
  // let idx = 0;
  // for (let i=0; i<callings.length; i++) {
  //     name = callings[i];
  //     idx = players.indexOf(name);
  //     players.splice(idx, 1);
  //     players.splice(idx - 1, 0, name);
  // }

  // map으로 변환
  const map = {};
  for (let i = 0; i < players.length; i++) {
    map[players[i]] = i;
  }

  for (const name of callings) {
    const idx = map[name];

    const prev = players[idx - 1];
    players[idx - 1] = name;
    players[idx] = prev;

    map[name] = idx - 1;
    map[prev] = idx;
  }

  return players;
}
