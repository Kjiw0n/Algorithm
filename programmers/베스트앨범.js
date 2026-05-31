// 1. 가장 많이 재생된 장르 찾기
// 1-1. 장르 별 재생 횟수 합
// 2. 각 장르 별 재생횟수 내림차순 정렬, 고유번호 오름차순 정렬
// 3. 각 장르 별 최대 두개만 수록

// N = 10^5

function solution(genres, plays) {
    const map = {}
    const total = {}
    
    for (let i=0; i<genres.length; i++) {
        (map[genres[i]] ??= []).push([i, plays[i]]) // [고유번호, 재생횟수]
        total[genres[i]] = (total[genres[i]] ?? 0) + plays[i]
    }
    
    const totalArr = []
    for (const key of Object.keys(total)) {
        totalArr.push([key, total[key]])
    }
    totalArr.sort((a, b) => b[1] - a[1])
    
    const ans = []
    for (const [genre, _] of totalArr) {
        const arr = map[genre]
        arr.sort((a, b) => b[1] - a[1] || a[0] - b[0])
        for (let i=0; i<(arr.length > 2 ? 2 : arr.length); i++) {
            ans.push(arr[i][0])
        }
    }
    
    return ans;
}