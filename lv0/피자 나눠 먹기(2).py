# 피자 나눠 먹기(2)
def solution(n):
    pizza = 1 # 피자 초기 값
    
    while (pizza*6) % n != 0:
        pizza += 1
    
    return pizza

  
import math

def solution(n):
    return (n * 6) // math.gcd(n, 6) // 6
