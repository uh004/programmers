# 제곱수 판별하기

import math

def solution(n):
    return 1 if int(math.sqrt(n)) ** 2 == n else 2

def solution(n):
    answer = 0
    for i in range(1,n):
        if int(i) * int(i) == int(n):
            return 1
    return 2
