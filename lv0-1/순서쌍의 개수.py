# n을 1 ~ n번까지 나눠서 나눠 떨어지면 그거는 순서쌍으로 포함된다.

def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n % i == 0:
            answer += 1
    
    return answer
