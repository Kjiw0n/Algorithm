function solution(elements) {
    const arr = [...elements, ...elements]
    const set = new Set()
    for (let i=1; i<(arr.length / 2) + 1; i++) {
        let sum = 0
        for (let j=0; j<i; j++) {
            sum += arr[j]
        }
        set.add(sum)
        for (let j=i; j<arr.length; j++) {
            sum -= arr[j - i]
            sum += arr[j]
            set.add(sum)
        }
    }
    
    return set.size;
}