function solution(sequence) {
    const cal = (p) => {
        let max = 0
        let sum = 0
        for (let i=0; i<sequence.length; i++) {
            sum = Math.max(sum + (sequence[i] * p), sequence[i] * p)
            p *= -1
            max = Math.max(max, sum)
        }
        return max
    }
    
    return Math.max(cal(1), cal(-1));
}