# 홀수를 기준으로 sort로 정렬하고
# 길이에서 2로 나누면 ex 5 // 2 = 2 이게인덱스가 0부터시작해서 가능

def solution(array):
    array.sort()
    return array[len(array)//2]
