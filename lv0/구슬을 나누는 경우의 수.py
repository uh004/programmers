# 구슬을 나누는 경우의 수

import math

def solution(balls, share):
    return math.comb(balls, share) # 조합 값 반환 nCk

from math import factorial as fac

def solution(balls, share):
    answer = 0
    n = fac(balls) # n!
    m = fac(share) # m!
    bottom = fac(balls - share) * m
    return n/bottom

