// N = 10^6

// number 순서대로 순회
// arr[-1]과 number[i] 비교
// 1. number[i]가 더 큰 경우
// 1-1. 더 작은 경우 만날 때까지 arr.pop()
// 1-2. pop 할 때마다 k-1
// 2. arr[-1]이 더 큰 경우 -> arr.push(num)
// 3. k 다썼는데 문자열 남은 경우 -> arr에 남은 문자열 전부 이어붙임


function solution(number, k) {
    const arr = []
    let i = 0
    
    for (i=0; i<number.length; i++) {
        while (arr.length > 0 && arr.at(-1) < number[i] && k > 0) {
            arr.pop()
            k--
        }
        arr.push(number[i])
    }
    
    while (k > 0 && i === number.length) {
        arr.pop()
        k--
    }
    
    return arr.join('');
}