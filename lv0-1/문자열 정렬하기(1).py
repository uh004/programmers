# 문자열 안에 숫자 판별 변수 number = 0~9까지 문자열로 숫자 넣고
# if문으로 my_string 값을 하나씩 비교 숫자가 들어있으면
# answer 리스트에 넣기

def solution(my_string):
    number = '0123456789'
    answer = []
    
    for i in my_string:
        if i in number:
            answer.append(int(i))
    answer.sort()       
    return answer

# 위에 코드를 한줄로 isdigit() 함수가 문자열안에 숫자판별 
def solution(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()])
