# 삼각형의 완성조건 (2)

def solution(sides):
    return sum(sides) - max(sides) + min(sides) - 1

def solution(sides):
    # 주어진 두 변의 길이
    x, y = min(sides), max(sides)

    # 나머지 한 변의 길이가 z일 때,
    # z가 가장 긴 변인 경우, y <= x < y+x
    # z가 가장 긴 변이 아닌 경우, y-x < z < y
    z = range(y-x+1, y+x)

    return len(z)

