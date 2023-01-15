# 문자 반복 출력

def solution(my_string, n):
    return ''.join(i*n for i in my_string)

def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i*n
    return answer
