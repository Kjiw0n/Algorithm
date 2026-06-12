// N = 10^5

// 먼 곳부터 채우고, 그 이하는 오는 길에 처리 -> 그리디

function solution(cap, n, deliveries, pickups) {
    let dl = n-1, pl = n-1 // 배달, 수거 끝 집
    let truck = cap // 트럭이 실은 상자 개수
    let dist = 0 // 이동 거리
    
    while (dl >= 0 || pl >= 0) {
        while (dl >= 0 && deliveries[dl] === 0) {
            dl--
        }
        while (pl >= 0 && pickups[pl] === 0) {
            pl--
        }
        
        dist += (Math.max(dl, pl) + 1)
        truck = cap
        
        for (let i=dl; i>=0; i--) {
            if (deliveries[i] >= truck) {
                deliveries[i] -= truck
                truck = 0
                break
            } else {
                truck -= deliveries[i]
                deliveries[i] = 0
            }
        }
        
        truck = cap
        for (let i=pl; i>=0; i--) {
            if (pickups[i] >= truck) {
                pickups[i] -= truck
                truck = 0
                break
            } else {
                truck -= pickups[i]
                pickups[i] = 0
            }
        }
    }
    
    return dist * 2;
}