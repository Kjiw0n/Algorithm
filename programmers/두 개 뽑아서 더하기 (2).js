function solution(numbers) {
    let arr = []
    
    // 100*100
    for(let i=0; i<numbers.length; i++) {
        for(let j=0; j<numbers.length; j++) {
            if (i === j) continue;
            arr.push(numbers[i] + numbers[j])
        }
    }
    
    arr = [...new Set(arr)]
    arr.sort((a, b) => a - b)
    
    return arr;
}