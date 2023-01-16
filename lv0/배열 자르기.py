# 배열 자르기

def solution(numbers, num1, num2):
    return numbers[num1:num2+1]

def solution(numbers, num1, num2):
    answer = []
    for i in numbers[num1:num2+1]:
        answer.append(i)

    return answer
