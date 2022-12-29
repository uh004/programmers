# 분수의 덧셈
def solution(denum1, num1, denum2, num2):
    answer = []
    # 1. 두 분수의 합 계산
    boonja = denum1 * num2 + denum2 * num1
    boonmo = num1 *num2
    
    # 2. 최대공약수 계산
    start = max(boonmo,boonja)
    gcd_value = 1
    
    for num in range(start,0,-1):
        if boonmo % num == 0 and boonja % num == 0:
            gcd_value = num
            break
    
    # 3. gcd 로 나눈 값을 answer에 담기
    answer = [boonja / gcd_value, boonmo / gcd_value]
    
    
    return answer

# ver2
def gcd(a,b):
    if a % b == 0:
        return b
    return gcd(b, a%b) # 재귀함수

def solution(denum1, num1, denum2, num2):
    answer = []
    # 1. 두 분수의 합 계산
    boonja = denum1 * num2 + denum2 * num1
    boonmo = num1 *num2
    
    # 2. 최대공약수 계산
    gcd_value = gcd(boonmo, boonja)

    # 3. gcd 로 나눈 값을 answer에 담기
    answer = [boonja / gcd_value, boonmo / gcd_value]
    return answer

# ver3
import math

def solution(denum1, num1, denum2, num2):
    answer = []
    # 1. 두 분수의 합 계산
    boonja = denum1 * num2 + denum2 * num1
    boonmo = num1 *num2
    
    # 2. 최대공약수 계산
    gcd_value = math.gcd(boonmo, boonja)

    # 3. gcd 로 나눈 값을 answer에 담기
    answer = [boonja / gcd_value, boonmo / gcd_value]
    return answer
