function solution(order) {
    const stack = []
    let head = 0 // order
    
    for (let box=1; box <= order.length; box++) {
        stack.push(box)
        
        while (stack.length > 0 && stack.at(-1) === order[head]) {
            stack.pop()
            head++
        }
    }
    
    return head;
}