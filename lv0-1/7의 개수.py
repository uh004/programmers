def solution(array):
    answer = ''
    
    for i in array:
        answer += str(i) # answer 변수에 i를 하나씩 문자열로 더하기
        
    return answer.count('7') # 문자열속에 7이 몇개있는지 count를 통해서 값 반환
    
