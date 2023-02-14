# st1안에 str2가 있다면이 조건이니까 if 조건문으로 검사

def solution(str1, str2):
    if str2 in str1:
        return 1
    else:
        return 2
# 위에 코드를 한줄로 변환하면
def solution(str1, str2):
    return 1 if str2 in str1 else 2
    
