function solution(Arr1, Arr2) {
    const a1 = Arr1.length, b1 = Arr1[0].length
    const a2 = Arr2.length, b2 = Arr2[0].length // a2 === b1
    
    const result = []
    
    for (let i=0; i<a1; i++) {
        const res = []
        for (let l=0; l<b2; l++) {
            let sum = 0
            for (let j=0; j<b1; j++) {
                sum += Arr1[i][j] * Arr2[j][l]
            }
            res.push(sum)
        }
        result.push(res)
    }
    
    return result;
}