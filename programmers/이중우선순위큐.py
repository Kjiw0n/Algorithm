import heapq

def solution(operations):
    hq_max = []
    hq_min = []
    deleted = set()
    for i, operation in enumerate(operations):
        command, n = operation.split(' ')
        n = int(n)
        if command == 'I':
            heapq.heappush(hq_max, (-n, i))
            heapq.heappush(hq_min, (n, i))
        else:
            if n == 1:
                while hq_max:
                    m, i = heapq.heappop(hq_max)
                    if i not in deleted:
                        deleted.add(i)
                        break
            else:
                while hq_min:
                    m, i = heapq.heappop(hq_min)
                    if i not in deleted:
                        deleted.add(i)
                        break
        
    ans = []
    for num, i in hq_min:
        if i not in deleted:
            ans.append(num)
    
    if len(ans) == 0:
        return [0, 0]
    else:
        return [max(ans), min(ans)]
