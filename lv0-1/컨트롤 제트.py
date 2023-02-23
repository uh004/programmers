def solution(s):
    answer = 0
    
    num = s.split(' ') # ['1','2','Z','3'] 으로 잘라서 리스트에 저장
    
    for i in range(len(num)): # 인덱스를 활용해서 num의 개수만큼 숫자 불러오기
        if num[i] == 'Z': # num[i] 번째가 Z랑 같으면 
            answer -= int(num[i-1]) # 전에 인덱스를 불러와서 빼주기
        else:
            answer += int(num[i]) # Z랑 같지 않으면 게속 더해주기
            
    return answer # 마지막값 반환
