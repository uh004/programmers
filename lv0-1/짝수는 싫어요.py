# 1 ~ n까지 반복해서 출력하고 range(시작값,마지막값,간격) 
# 우리는 짝수 빼고 출력이니까 1부터 n까지 2간격으로하면 된다.
def solution(n):
    answer = []
    
    for i in range(1,n+1,2):
        answer.append(i)
    return answer
  
# 위에 코드를 컴플레헨션으로 줄이면 아래 코드
def solution(n):
    answer = [i for i in range(1,n+1,2)]
    return answer

# 이 코드는 2로 나누어 떨어지지 않는게 홀수로 조건표시
def solution(n):
    answer = [i for i in range(1,n+1) if i % 2 != 0]
    return answer
