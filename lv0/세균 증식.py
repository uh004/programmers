# 세균 증식

def solution(n, t):
    for  _ in range(1,t+1):
        n = n * 2
    
    return n

# 비트연산자 활용
def solution(n, t):
    return n << t
