// progresses 다 비울 까지 반복
// 1. speeds 순회하며 각 progresses에 추가
// 2. progresses[0]이 100을 넘을 때마다 shift, cnt++
// 3. cnt개 배포, cnt는 다시 0으로 초기화

function solution(progresses, speeds) {
    const ans = []
    let head = 0
    while (head < progresses.length) {
        let cnt = 0
        
        for (let i=head; i<progresses.length; i++) {
            progresses[i] += speeds[i]
        }
        
        for (let i=head; i<progresses.length; i++) {
            if (progresses[i] >= 100) {
                head++
                cnt++
            } else {
                break
            }
        }
        
        if (cnt > 0) {
            ans.push(cnt)
        }
    }
    
    return ans;
}