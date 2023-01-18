# 컨트롤 제트

def solution(s):
    answer = 0
    num = s.split(' ') 
    for i in range(len(num)):
        if num[i] == 'Z':
            answer -= int(num[i-1])
        else:
            answer += int(num[i])
    
    return answer
