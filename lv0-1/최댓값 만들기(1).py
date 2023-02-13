# 그냥 sorted로하면 작은순부터 커져서 이걸 반대로 바꿔서
# 큰수부터 나란하게 만들고 첫번째 두번째 인덱스를 곱해서 반환하면 값이 나온다.

def solution(numbers):
    answer = sorted(numbers, reverse =True)
    
    return answer[0] * answer[1]
