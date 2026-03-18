// Todo: 크레인으로 바구니에 인형, 같은 인형 담기면 터트리기
// return: 터진 인형 개수

// board 배열은 2차원 배열로 크기는 "5 x 5" 이상 "30 x 30" 이하
// moves 배열의 크기는 1 이상 1,000 이하
// -> N^3 까지 가능

// 1. moves에 따라 인형 뽑기
// 1-1. 맨 위에 있는 인형 뽑기
// 2. 뽑은 인형을 바구니에 넣기
// 2-2. 같은 인형 연속으로 담기면 터트리기
// 2-3. 터트린 인형 개수 세기
// 3. 터트인 인형 개수 리턴

function solution(board, moves) {
    const N = board.length
    const graph = []
    for (let i=0; i<N; i++) {
        const arr = []
        for (let j=N-1; j>=0; j--) {
            if (board[j][i] === 0) continue
            arr.push(board[j][i])
        }
        graph.push(arr)
    }
    
    const stack = []
    let cnt = 0
    
    for (const move of moves) {
        if (graph[move - 1].length === 0) {
            continue
        }
        const a = graph[move - 1].pop()
        if (stack.length > 0 && stack.at(-1) === a) {
            stack.pop()
            cnt += 2
        } else {
            stack.push(a)
        }
    }
    
    return cnt;
}