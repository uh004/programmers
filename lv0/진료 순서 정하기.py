# 진료 순서 정하기

def solution(emergency):
    answer = []
    tmp = sorted(emergency, reverse= True)
    
    for i in emergency:
        answer.append(tmp.index(i)+1)
    return answer

def solution(emergency):
    e = sorted(emergency,reverse=True)
    return [e.index(i)+1 for i in emergency]
