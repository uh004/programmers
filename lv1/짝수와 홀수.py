# 입력받은 num은 2로 나눠떨어지면 짝수 아니면 홀수

def solution(num):
    
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
      
# 위에 코드를 한줄로 컴플리헨션으로 변경
def solution(num):
    return 'Even' if num %2 == 0 else 'Odd'
