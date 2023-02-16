def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper(): # isupper() 대문자 감지
            answer += i.lower() # 대문자면 소문자로
        else:
            answer += i.upper() # 소문자면 대문자로
    return answer
