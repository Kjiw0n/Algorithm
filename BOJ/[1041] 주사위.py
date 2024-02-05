N = int(input())

dice_input = list(map(int, input().split()))

if N == 1:
    N1dice = sorted(dice_input)
    print(sum(N1dice[0:5]))
else:

    # 면이 3개인 주사위는 몇개?
    # 항상 4개
    surface_3 = 4

    # 면이 2개인 주사위는 몇개?
    # (N - 2) * 4<맨 윗줄> + (N - 1) * 4<맨 윗줄 제외 테두리> = (2N - 3) * 4
    surface_2 = (2 * N - 3) * 4

    # 면이 1개인 주사위는 몇개?
    # (N*N - (3N-2)) * 4 + N*N - (4N-4) = 5N*N - 16N + 12
    surface_1 = 5 * N * N - 16 * N + 12

    # 면이 0개인 주사위는 몇개?
    # 아예 안보이는 주사위도 있음
    # 계산할 필요는 x

    surface = [surface_1, surface_2, surface_3]

    # sort가 아니야
    # 맞닿는 면의 합 중 최소가 될 수 있도록..
    # A B C D E F 를 숫자로 표현할 때, 1 2 3 4 5 6 중 (1, 6), (2, 5), (3, 4)은 같이 선택 안됨
    # 인덱스로는 (0, 5), (1, 4), (2, 3)
    min_set = (min(dice_input[0], dice_input[5]),
               min(dice_input[1], dice_input[4]),
               min(dice_input[2], dice_input[3]))

    min_set = sorted(min_set)
    sum_surface = 0
    result = 0
    for i in range(3):
        sum_surface += min_set[i]
        result += sum_surface * surface[i]

    print(result)
