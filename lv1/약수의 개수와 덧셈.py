def solution(left, right):

    number = 0
    for i in range(left,right+1): # 13 ~ 18
        answer = 0 # 약수 개수 카운팅 for문 안에 넣어줘야 0으로 초기화
        for j in range(1,i+1): # 1 ~ 14
            if i % j == 0: # i 가 1부터 i까지 나눠떨어지면 약수
                answer += 1 # 약수개수 더해주기
                
        if answer % 2 == 0: # 약수개수가 2로 나눠 떨어지면 짝수 
            number += i # 더해주기
        else: # 홀수면 마이너스
            number -= i # 마이너스
                
    return number
