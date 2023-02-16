# 최대한 많은 정육면체를 만들고 싶어한다.
# 가로 세로 높이 모서리 길이 = n
# 가로 세로 높이를 모서리로 나눠서 몫값만 다 곱해주

def solution(box, n):
    answer = 1
    for i in box:
        answer *= i // n
    return answer
  
# divmod함수를 사용해서 몫 나머지 중에 몫만 곱해주기
def solution(box, n):
    answer = 1
    for i in box:
        answer *= divmod(i,n)[0]
    return answer
