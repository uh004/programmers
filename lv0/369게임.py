# 369게임

def solution(order):
    answer = 0
    num = '369'
    for i in str(order):
        if i in num:
            answer += 1
    
    return answer

def solution(order):
    answer = 0
    for i in str(order):
        if int(i)!=0 and int(i)%3==0:
            answer+=1
    return answer
