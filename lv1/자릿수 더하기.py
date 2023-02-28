# 자릿수 더하기 ex) 123 -> 6
# 123을 문자열로 불러와 for문으로 하나씩 불러오고
# 불러온 문자를 정수형으로 바꿔서 더하기

def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)

    return answer
