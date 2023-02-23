def solution(my_str, n):
    answer = [] # n개씩 
    
    for _ in range(0,len(my_str),n): # 0,부터 n의 개수만큼 n만큼 증가
        answer.append(my_str[:n]) # 첨부터 n까지 문자열 저장
        my_str = my_str[n:] # 0 0 0 0 0 0 -> 인덱스 n까지 저장한거 그 이후거로 다시 저
        
    return answer
