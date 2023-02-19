# 문자열 a~z까지 하나씩 불러와서 
# 조건에 s에 count함수를 이용해서 c로 하나씩 불러온게 몇개인지 
# 확인하기 

def solution(s):
    answer = ''
    s = sorted(s)
    
    for i in s:
        if s.count(i) == 1:
            answer += i
    
    return answer
  
def solution(s):
    answer = ''
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if s.count(c) == 1:
            answer += c
    return answer
