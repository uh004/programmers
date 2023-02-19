# tmp변수에 큰수보다 정렬하기 
# for문으로 emergency하나씩 불러와서 tmp로 정렬하고 index로 확인하기 
# 진료순서를 하나씩 더하기 인덱스가 0부터시작해서 +1 더해주기

def solution(emergency):
    answer = []
    tmp = sorted(emergency, reverse= True)
    
    # tmp = 76 24 3  emergency = 3 76 24 
    for i in emergency:
        answer.append(tmp.index(i)+1)
    return answer

def solution(emergency):
    answer = []
    sort_num = sorted(emergency, reverse = True)

    for i in emergency:
        answer.append(sort_num.index(i) + 1)

    return answer
