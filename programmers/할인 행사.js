function solution(want, number, discount) {
    const wish = {}
    for (let i=0; i<want.length; i++) {
        wish[want[i]] = number[i]
    }
    
    const cur = {}
    for (let i=0; i<10; i++) {
        cur[discount[i]] = (cur[discount[i]] ?? 0) + 1
    }
    
    let cnt = 0
    for (let i=10; i<=discount.length; i++) {
        let flag = true
        for (const key in wish) {
            if (wish[key] != cur[key]) {
                flag = false
                break
            }   
        }
        if (flag) cnt++
        if (i === discount.length) break
        
        cur[discount[i - 10]]--
        cur[discount[i]] = (cur[discount[i]] ?? 0) + 1
    }
        
    return cnt;
}