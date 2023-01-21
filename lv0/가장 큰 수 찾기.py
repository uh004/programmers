# 가장 큰 수 찾기

def solution(array):
    m = max(array)
    i = array.index(m)
    answer = [m, i]
    return answer

def solution(array):
    return [max(array), array.index(max(array))]
