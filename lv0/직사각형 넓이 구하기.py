# 직사각형 넓이 구하기

def solution(dots):
    x = [i[0] for i in dots]
    y = [i[1] for i in dots]
    return (max(x)-min(x))*(max(y)-min(y))

def solution(dots):
    x, y = [], []
    for dot in dots:
        x.append(dot[0])
        y.append(dot[1])
    return (max(x) - min(x)) * (max(y) - min(y))
