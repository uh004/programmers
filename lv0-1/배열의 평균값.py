# 평균값 구하는 식 = 모든수 더하고 그 값에 길이만큼 나누면 된다.
def solution(numbers):
    return sum(numbers) / len(numbers)

# numpy 라이버러리 활용 라이브러리 많이 알아두면 좋다
import numpy as np
def solution(numbers):
    return np.mean(numbers)
