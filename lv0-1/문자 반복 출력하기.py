# 문자 반복 for문을 이용해서 하나문자를 불러와서 n번만큼 곱하고 다시 변수에 담아서 이어서 붙이기

def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i*n
    return answer

# 컴플리헨션을 통해 join으로 이어붙이기
def solution(my_string, n):
    return ''.join(i*n for i in my_string)
