dice = list(map(int, input().split()))
set_dice = set(dice)

if len(set_dice) == 1:
    print(10000 + dice[0] * 1000)
elif len(set_dice) == 2:
    if dice[0] == dice[1]:
        print(1000 + dice[0] * 100)
    elif dice[0] == dice[2]:
        print(1000 + dice[0] * 100)
    elif dice[1] == dice[2]:
        print(1000 + dice[1] * 100)
else:
    print(max(dice) * 100)

