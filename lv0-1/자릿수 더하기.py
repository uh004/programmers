# for문을 이용해서 n을 문자열로 바꿔서 하나씩 불러오기
# 불러온 숫자를 다시 int로 바꿔서 더하고 반환
def solution(n):
    answer = 0
    n = str(n)
    for i in n:
        answer += int(i)
        
    return answer
# 위에 코드를 한줄로 변환하면 이렇게
def solution(n):
    return sum(int(i) for i in str(n))
