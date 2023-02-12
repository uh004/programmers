# numbers가주어지고  인덱스 num1부터 num2까지 인덱스 출력

def solution(numbers, num1, num2):
    answer = []
    for i in numbers[num1:num2+1]:
        answer.append(i)

    return answer

def solution(numbers, num1, num2):
    return [i for i in numbers[num1:num2+1]]
