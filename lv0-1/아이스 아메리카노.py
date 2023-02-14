# 리스트컴플리헨션으로 인덱스 0번째는 몫 값 1번째는 나머지
def solution(money):
    return [money // 5500, money % 5500]
  
# num1 잔수 num2 남은 돈 해서 입력받은 머니를 몫과 나머지로 반환
def solution(money):
    num1 = 0 # 잔수 
    num2 = 0 # 남은 돈
    
    num1 = money // 5500
    num2 = money % 5500
    
    return [num1,num2]
