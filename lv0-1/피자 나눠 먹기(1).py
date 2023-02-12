# math 라이브러리 활용 피자계수가 딱 나눠 떨어질수가 있으나 소수점이 남으면
# 무조건 한사람당 하나는 먹어야하니까 올림함수를 사용

import math

def solution(n):
    
    return math.ceil(n / 7)

  # if 문을 사용해서 몫이 0이면 나머지만 몫이 1이면 몫 + 1로 남은 사람도 먹을수있게
  
def solution(n):
    answer = 0
    if n % 7 == 0:
        answer = n // 7
    else:
        answer = (n // 7) + 1
    return answer
