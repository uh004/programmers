# 문자열 정렬하기 (1)

def solution(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()]) # isdigit 숫자 판별

def solution(my_string):
    answer = '0123456789'
    num = []
    
    for i in my_string:
        if i in answer:
            num.append(int(i))
    num.sort()    
    return num
