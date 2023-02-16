from collections import deque as dq

def solution(numbers, direction):
    numbers = dq(numbers)
    if direction == 'right':
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)

# 오right면 오른쪽으로 옮겨야하니까 
def solution(numbers, direction):
    answer = []
    if direction == 'right':
        numbers = numbers[-1:] + numbers[:-1]
    else:
        numbers = numbers[1:] + numbers[:1]
    return numbers
