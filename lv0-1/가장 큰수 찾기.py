# max(array) -> 제일 큰 수
# 인덱스를 if문으로 number 인덱스 0부터 시작 
# 큰수를 같은지 비교해서 같으면 멈추기

def solution(array):
    number = 0
    answer = max(array)
    
    for i in array:
        if i == answer:
            break
        number += 1
    
    return [answer,number]

# index -> 파이썬 내장되있는 원하는 값 찾
def solution(array):
    return [max(array), array.index(max(array))]
