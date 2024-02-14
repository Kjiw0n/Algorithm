from collections import Counter

words = []
while True:
    word = input()
    if word == '-':
        break
    words.append(sorted(word))

puzzles = []
while True:
    puzzle = input()
    if puzzle == '#':
        break
    puzzles.append(sorted(puzzle))

# (x)집합으로 처리하면 되겠네!!
#    일단 puzzle의 값을 포함하고 있는지? 포함 x 단어는 제외 -> 차집합 != 공집합 -> 그 단어 뺴기
# 이유: 근데 뺄 때 예외처리 못하는 부분이 한 글자 당 최대 1번 사용.. if 퍼즐에 O가 1번 있는데, word는 OOP인 경우에 오류

# 사전순으로 나열 후 알파벳(인덱스)가 puzzle이랑 같으면 다음으로 알파벳으로: 하나하나 비교
# (!!) 개수 count 할 때 Counter 라이브러리 쓰면 됨.........

def find_word(word, puzzle):
    word_count = Counter(word)
    puzzle_count = Counter(puzzle)

    for char, count in word_count.items():
        if puzzle_count[char] < count:
            return False
    return True

result = []

for puzzle in puzzles:
    puzzle_word = []
    for word in words:
        if find_word(word, puzzle):
            puzzle_word.append(word)

    re_count = [0] * len(puzzle)
    for p in puzzle_word:
        for i in range(len(puzzle)):
            if p.count(puzzle[i]) != 0:
                re_count[i] += 1

    min_count = min(re_count)
    max_count = max(re_count)
    result_min = ''
    result_max = ''
    for i in range(len(puzzle)):
        if re_count[i] == min_count and result_min.count(puzzle[i]) == 0:
            result_min += puzzle[i]
        if re_count[i] == max_count and result_max.count(puzzle[i]) == 0:
            result_max += puzzle[i]

    result.append([result_min, min_count, result_max, max_count])

for r in result:
    print(*r)
