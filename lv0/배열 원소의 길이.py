# 배열 원소의 길이

def solution(strlist):
    answer =[]
    for i in strlist:
        answer.append(len(i))
    return answer

def solution(strlist):
    answer = []
    num = 0
    for i in strlist:
        for j in i:
            num += 1
        answer.append(num)
        num = 0
    
    return answer
