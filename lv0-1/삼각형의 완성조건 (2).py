# 나중에 다시 풀기

def solution(sides):
    answer = 0
    return sum(sides) - (max(sides) - min(sides)) -1
