def solution(x, n):
    answer = [] # 
    
    for i in range(1,n+1):# 1 부터 n까지 
        answer.append(x*i) # x곱하기 1부터 n개수만큼 5면 1~5가 answer에 저장
    
    return answer
