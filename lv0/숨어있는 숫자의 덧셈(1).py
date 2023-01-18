# 숨어있는 숫자의 덧셈 (1)

def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())

def solution(my_string):
    answer = '0123456789'
    num = []
    
    for i in my_string:
        if i in answer:
            num.append(int(i))
    
    return sum(num)
