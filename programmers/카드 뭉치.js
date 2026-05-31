// 필요한 단어가 없으면 No 리턴
// 필요한 단어가 있으면 head1, head2 관리 (큐)

function solution(cards1, cards2, goal) {
    let head1 = 0
    let head2 = 0
    
    const len1 = cards1.length
    const len2 = cards2.length
    
    for (let i=0; i<goal.length; i++) {
        if (head1 < len1 && goal[i] === cards1[head1]) head1++
        else if (head2 < len2 && goal[i] === cards2[head2]) head2++
        else return 'No'
    }
    
    return 'Yes';
}