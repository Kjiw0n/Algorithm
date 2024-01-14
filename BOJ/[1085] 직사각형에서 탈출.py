x, y, w, h = map(int, input().split())

# 오른쪽 경계 ~ 현재 위치, 윗쪽 경계 ~ 현재, 왼쪽~, 아래쪽~
result = min((w - x), (h - y), x, y)

print(result)