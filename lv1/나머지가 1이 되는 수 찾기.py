# n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 조건


def solution(n):
    answer = 0
    
    for i in range(1,n+1): # 1부터 n까지 불러와서
        if n % i == 1: # n을 1부터 n까지 불러온 수중에 나머지가 1이되면 반환
            answer += i
            break # 가장작은 자연수니까 먼저 1되고 정지시키기
    
    return answer
