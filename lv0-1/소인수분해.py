def solution(n):
    answer = [] # 소인수분해 넣기
    number = 2 # 소인수분해 2부터 시작
    
    while number <= n: # 조건이 number가 더크면 반복 종료
        if n % number == 0: # 나머지가 0이면 소인수 분해
            answer.append(number)
            n = n // number # 나눠 떨어진거에 몫으로 나누고 다시 반환
        else:
            number += 1 # 안나눠떨어지면 number값 +1씩 더하기
            
    return list(set(answer))
