function solution(array, commands) {
    const ans = []
    for (const [i, j, k] of commands) {
        const arr = array.slice(i - 1, j)
        arr.sort((a, b) => a - b)
        ans.push(arr[k - 1])
    }
    
    return ans;
}