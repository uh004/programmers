# 5 3 1 이라는 개미가 효율적으로 몇명 데려갈지 포함

def solution(hp):
    num1 = hp // 5
    num2 = hp % 5 // 3
    num3 = hp % 5 % 3 // 1
    
    return num1 + num2 + num3

# divmod함수를 이용해서 몫,나머지로 몫만 더하기
  
def solution(hp):
    answer = 0
    for ant in [5, 3, 1]:
        d, hp = divmod(hp, ant)
        answer += d
    return answer
