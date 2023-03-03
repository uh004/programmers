def solution(arr, divisor):
    answer = [] # 나누어 떨어지는 수 대입
    arr.sort() # arr 정렬
    
    for i in arr:
        if i % divisor == 0: 
            answer.append(i) # arr에 하나씩 불러온게 divsior로 나눠떨어지면 answer에 저장
            
    if len(answer) == 0: # for문이 끝나고 answer에 하나도 없으면 -1 반환 형식으로
        return [-1]
    else:
        return answer
