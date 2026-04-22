# 베스트 앨범에 들어갈 노래의 고유 번호 배열 리턴

# 1. 각 장르 별 딕셔너리화 key - [고유번호, 플래이 수]
# 2. sum 기준 내림차순 정렬 -> 각 아이템 별 (-플래이 수, 고유번호) 정렬
# 3. 앞에서부터 두개씩만 수록

# N = 10^4, O(NlogN)

from collections import defaultdict

def solution(genres, plays):
    genre_dict = defaultdict(list)
    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_dict[genre].append((i, play))
    
    sorted_by_genre = sorted(genre_dict.items(), key=lambda x: sum(play for _, play in x[1]), reverse=True)
    
    ans = []
    for item in sorted_by_genre:
        item[1].sort(key=lambda x: (-x[1], x[0]))
        print(item)
        idx = 0
        for i, _ in item[1]:
            if idx >= 2: break
            ans.append(i)
            idx += 1
    
    return ans