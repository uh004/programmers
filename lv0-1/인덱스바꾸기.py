# 인덱스를 활용해서 my_string을 리스트로 하나씩 바꾸고
# 파이썬에서는 num1,num2 = num2,num1 을 바꿀수 있다.
# 바꾸고 join으로 문자열 묶기
# 다른언어는 다른변수  만들어서 num0 = num1 -> num1 = num2 -> num2 = num0 식으로 바꾸기

def solution(my_string, num1, num2):
    my_string = list(my_string)
    my_string[num1],my_string[num2] = my_string[num2],my_string[num1]
    return ''.join(my_string)
