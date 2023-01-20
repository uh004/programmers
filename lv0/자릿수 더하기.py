# 자릿수 더하기

def solution(n):
    return sum(int(i) for i in str(n))

def solution(n):
    answer = 0
    
    for i in str(n):
        answer += int(i)
    
    return answer
