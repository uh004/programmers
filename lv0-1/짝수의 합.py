# 파이썬 컴프리헨션 이용 if문해서 2로 나눠떨어지면 짝수만 더함
def solution(n):
    return sum([i for i in range(2, n+1) if i % 2 ==0]) 

  # 파이썬 컴프리헨션 이용 짝수부터니까 2부터 range(시작 값, 끝 값, 간격) 간격을2 주면 짝수만 더함
def solution(n):
    return sum([i for i in range(2, n + 1, 2)])
