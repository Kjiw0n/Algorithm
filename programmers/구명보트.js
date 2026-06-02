// N = 5*10^4

// people 오름차순으로 정렬
// people[head] + people[rear] < limit => rear--하면서 가능한 경우 찾기


function solution(people, limit) {
    people.sort((a, b) => a - b)
    let head = 0
    let rear = people.length - 1
    let cnt = 0
    
    while (head <= rear) {
        if (people[head] + people[rear] <= limit) head++
        rear--
        cnt++
    }
    
    return cnt;
}