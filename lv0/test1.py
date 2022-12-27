def solution(array, n): # [1, 1, 2, 3, 4, 5]	1
    answer = 0
    for i in array: # 하나씩 꺼냄
        if i == n:
            answer += 1
    return answer

def solution(array, n): # [1, 1, 2, 3, 4, 5]	1
    answer = 0
    for i in range(len(array)):
        if array[i] == n:
            answer += 1
    return answer
