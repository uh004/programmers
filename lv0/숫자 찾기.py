# 숫자 찾기

def solution(num, k):
    a = str(num).find(str(k)) # 문자열 찾기 반환
    return (a if a == -1 else a+1)
