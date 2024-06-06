N, M = map(int, input().split())

dic = {}
# 아니 그냥 하나의 dic에 key로 팀 이름, value로 멤버 리스트 넣고
# if 멤버이름 in dic 이런 식으로 쓰면안되나

for _ in range(N):
    s = input()
    n = int(input())
    member = []
    for _ in range(n):
        member.append(input())

    dic[s] = sorted(member)

# print(dic)

for i in range(M):
    s = input()
    n = int(input())

    if n == 0:
        # 멤버들 찾기
        print('\n'.join(dic[s]))
    else:
        # 팀 찾기
        for team, members in dic.items():
            if s in members:
                print(team)
                break

