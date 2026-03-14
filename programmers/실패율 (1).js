// 배경
// 문제: 신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무 큰 것
// 해결: 동적으로 게임 시간 늘려서 난이도 조절

// Todo: 실패율을 구하기
// 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
// return: 스테이지의 번호가 담겨있는 배열 (실패율이 높은 스테이지부터 내림차순)

// stages.length: 총 사용자 수

// 1. 스테이지 별로 도전 중인 사용자 수 각각 구하기
// 2. 스테이지 올라갈수록 총 사용사 수에서 직전 스테이지 도전 중인 사용자 수 빼기
// 3. 각 스테이지 별 실패율을 저장 (스테이지번호: 실패율)
// 4. 내림차순으로 정렬하여 스테이지 번호 출력

function solution(N, stages) {
    let M = stages.length
    const challenges = new Array(N + 1).fill(0)    
    
    for (const stage of stages) {
        challenges[stage - 1]++;
    }
    
    const fails = []
    for (let i=0; i<N; i++) {
        perc = challenges[i] / M
        fails.push([i + 1, perc])
        M -= challenges[i]
    }
    return fails.sort((a, b) => b[1] - a[1] || a[0] - b[0]).map(v => v[0])
}