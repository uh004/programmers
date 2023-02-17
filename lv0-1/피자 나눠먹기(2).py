# pizaa 6개로 쪼갠다 num = 초기피자 한판
# pizza를 n으로나눠 떨어지면 다같이 먹는다 break 걸고
# 게속 한판 늘릴때마다 6조각 씩 쪼개는걸로 

def solution(n):
    pizza = 6
    num = 1
    
    for _ in range(1,n):
        if pizza % n == 0:
            break
        pizza += 6
        num +=1
    
    return num

# 위에랑 비슷하게 조건이 pizza를 n으로 나눴을때 나눠떨어질때까지
# 0이랑 같으면 조건이 끝나는걸로
def solution(n):
    pizza = 1 # 피자 초기 값
    
    while (pizza*6) % n != 0:
        pizza += 1
    
    return pizza
    
