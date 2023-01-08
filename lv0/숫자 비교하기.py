# 숫자 비교하기
def solution(num1, num2):
    answer = 0
    if num1 != num2:
        answer = -1
    elif num1 == num2:
        answer = 1
    return answer
