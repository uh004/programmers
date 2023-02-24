# 조합 공식 n! / (n-m)! x m! 3 2  6 / 2 = 3

from math import factorial as fac

def solution(balls, share):
    answer = 0
    n = fac(balls) # n! # n 팩토리얼
    m = fac(share) # m! # m 팩토리얼
    bottom = fac(balls - share) * m # 바텀 팩토리얼 (n-m)! x m!
    return n/bottom
