# 369를 확인하려면 문자열로 바꾸고 하나씩 불러와서
# 369에 포함되있으면 변수에 1 더하는식으로

def solution(order):
    answer = 0
    
    for i in str(order):
        if i in '369':
            answer += 1
    
    return answer
# count함수를 통해 문자열로 바꿔서 계수 더하기
def solution(order):
    answer = 0
    order = str(order)
    return order.count('3') + order.count('6') + order.count('9')
