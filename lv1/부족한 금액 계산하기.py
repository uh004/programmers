def solution(price, money, count):
    answer = 0 # 이용료 N배의 값
    
    for i in range(1,count+1):
        answer += price * i # count 할때마다 가격이 게속 더해져서 저장
        
    if money - answer < 0: # 조건이 금액이 부족하지 않으면 이니까 뺏을때 마이너스가 되면 모자른다
        return abs(money - answer) # 절대값 붙혀서
    else:
        return 0 # 만약에 0보다 크면 금액이 부족하지 않음 그래서 0반환
