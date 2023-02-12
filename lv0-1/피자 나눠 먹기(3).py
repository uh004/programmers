# slice 피자 조각 수 n 먹는 사람 
# 최소 n명이 한조각씩 먹을수 있게 
# n / slice 나누기 이제 소수가 나오면 올림으로 그사람도 먹을수 있게 반환

import math

def solution(slice, n):
    
    return math.ceil(n / slice)

# n // slice를 하고 나머지를 비교 0이면 딱 나눠 떨어져서 바로 몫 값 출력
# 나머지가 0이 아니면 남은 사람수가 있으니 나눈 몫 + 1 반환
  
def solution(slice, n):
    answer = n//slice

    if n%slice != 0:
        answer +=1

    return answer
