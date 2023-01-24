# 가까운 수

def solution(array,n):
    array.sort()
    answer = 0
    answer = min(array, key= lambda x:abs(x-n))
    return answer

def solution(array, n):
    array.sort(key = lambda x : (abs(x-n), x-n))
    answer = array[0]
    return answer
