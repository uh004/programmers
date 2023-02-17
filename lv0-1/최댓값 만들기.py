# sort함수로 인덱스가 0부터 크게 만들고  
# 인덱스 0 * 1 이랑 마이너스도 있어서 -1 * -2 인덱스를 
# max함수로 둘중에 큰거를 반환

def solution(numbers):
    answer = 0
    numbers.sort(reverse=True)
    answer = max(numbers[0] * numbers[1],numbers[-1] * numbers[-2])
    return answer
