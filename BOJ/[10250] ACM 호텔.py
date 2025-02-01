T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    room = [N % H, N // H + 1]

    if room[0] == 0:
        room[0] = H
        room[1] -= 1

    print(f"{room[0]}{room[1]:02d}")