// N = 10^4, M = 6*10^4

// i번째 진출점에 1개, i+1번째 차량 진입점이 마지막 카메라(last)보다 뒤면 진출점에 추가 설치

function solution(routes) {
    routes.sort((a, b) => a[1] - b[1])
    let last = routes[0][1]
    let cnt = 1
    
    for (let i=1; i<routes.length; i++) {
        if (last < routes[i][0]) {
            console.log(routes[i][1])
            last = routes[i][1]
            cnt++
        }
    }
    
    return cnt;
}