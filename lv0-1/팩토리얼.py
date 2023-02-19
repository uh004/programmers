# answer -> 1~ n까지 커지고 
# fac는 곱한거 n과 비교해서 n보다 커지면 팩토리얼 반복문 종료
# 마지막에 answer - 1 하는 이유는 그 수보다 커지면 종료되니까
# 그전까지가 조건이 되서 이런식이 나왔다.

def solution(n):
    answer = 1
    fac = 1
    while fac <= n :
        answer += 1
        fac = fac * answer
    answer = answer-1
    
    return answer
