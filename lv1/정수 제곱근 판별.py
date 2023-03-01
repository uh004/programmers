# 코드는 실행 되는데 제출하면 마지막게 안되서 99퍼 실행

def solution(n):    
    answer = -1
    
    for i in range(1,n):
        if i ** 2 == n:
            answer = int((i+1)**2)
            break

        
    return answer

# 다른 사람 풀이
  def solution(n):
    
    a = (n**0.5)
    
    if a % 1 == 0:
        answer = (a+1)**2
    else:
        answer = -1
        
    return answer
