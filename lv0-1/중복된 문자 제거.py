# 중복된 문자제거 
# for문으로 문자열 하나씩 불러와서 if조건으로 answr에 없으면 추가하게
# 만약에 그 문자가 있으면 if문 실행안함

def solution(my_string):
    answer = ''
    
    for i in my_string:
        if i not in answer:
            answer += i
            
    return answer
