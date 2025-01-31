def solution(wallet, bill):
    answer = 0

    while max(wallet) < max(bill) or min(wallet) < min(bill):
        i = bill.index(max(bill))
        bill[i] //= 2
        answer += 1

    return answer