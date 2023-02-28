def solution(s):
    answer = True # num1 != num2 개수가 다르면 false로 변경
    num1 = 0 # 문자열 'p' 'P' 개수 저장
    num2 = 0 # 문자열 'y' 'Y' 개수 저장
    
    for i in s: # s에 문자열 하나씩 불러오기
        if i == 'p' or i == 'P': # i 가 p,P인지 확인
            num1 += 1 # p,P가 맞으면 +1
        elif i == 'y' or i == 'Y': # i가 y,Y인지 확인
            num2 += 1 # y,Y가 맞으면 + 1
            
    if num1 != num2: # q와y 개수 비교 
        answer = False # 개수가 안맞으면 false로 변경
        
    return answer
