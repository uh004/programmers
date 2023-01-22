# 문자열 정렬하기 (2)

def solution(my_string):
    return ''.join(sorted(my_string.lower()))

def solution(my_string):
    my_string = sorted(list(my_string.lower()))
    answer = ''.join(my_string)
    
    return answer
