# 최댓값 만들기 (1)

def solution(numbers):
    numbers.sort(reverse=True)
    return numbers[0]*numbers[1]

def solution(numbers):
    answer = sorted(numbers, reverse =True)
    
    return answer[0] * answer[1]
