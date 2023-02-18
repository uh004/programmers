# sorted함수로 정렬하고 소문자로 바꾸는함수 lower list로 만들고
# join으로 붙이기

def solution(my_string):
    my_string = sorted(list(my_string.lower()))
    answer = ''.join(my_string)
    
    return answer
  
# 위 코드를 한줄로
def solution(my_string):
    return ''.join(sorted(my_string.lower()))
