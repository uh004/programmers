# 1시간 마다 배씩 증가 n에 게속 2를 곱하기

def solution(n, t):
    for _ in range(1,t+1):
        n = n * 2
        
    return n

# 비트 연산을 활용
def solution(n, t):
    return n << t
