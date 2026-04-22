# 완주 못한 선수 이름 리턴
# 이름순 정렬 후 다른 이름 나오면 참여자쪽 이름 리턴

# N = 10^5 -> O(NlogN)

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i, p in enumerate(participant):
        if i >= len(completion) or p != completion[i]:
            return p
    