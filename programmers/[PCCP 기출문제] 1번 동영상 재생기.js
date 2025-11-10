const paserTimeToNum = (arr) => {
    return Number(arr.split(':')[0]) * 60 + Number(arr.split(':')[1])
}

function solution(video_len, pos, op_start, op_end, commands) {
    let video_t = paserTimeToNum(video_len)
    let pos_t = paserTimeToNum(pos)
    let op_start_t = paserTimeToNum(op_start)
    let op_end_t = paserTimeToNum(op_end)
    
    for (const command of commands) {
        if ((pos_t >= op_start_t) && (pos_t <= op_end_t)) {
            pos_t = op_end_t
        }
        if (command === 'prev') {
            pos_t = pos_t - 10 < 0 ? 0 : pos_t - 10
        } else {
            pos_t = pos_t + 10 > video_t ? video_t : pos_t + 10
        }
    }
    if ((pos_t >= op_start_t) && (pos_t <= op_end_t)) {
        pos_t = op_end_t
    }
    
    const s = pos_t % 60
    const m = (pos_t - s) / 60
    
    let mm = m < 10 ? '0' + m.toString() : m.toString()
    let ss = s < 10 ? '0' + s.toString() : s.toString()
    return mm + ':' + ss;
}