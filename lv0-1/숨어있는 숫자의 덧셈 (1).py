# 문자열안에 숫자 확인하려고 number 0~9까지 문자열 생성
# for문으로 my_string 문자열 하나씩 불러와서 if 조건으로 i가 0~9까지 있으면
# i를 숫자로 바꿔서 answer에 더하는식으로

def solution(my_string):
    number = '0123456789'
    answer = 0
    for i in my_string:
        if i in number:
            answer += int(i)
            
    return answer
