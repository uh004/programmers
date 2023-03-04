def solution(numbers):
    answer = 45 # 0~9 까지 총합
    
    for i in numbers:
        if str(i) in '0123456789': # 문자열로 바꿔서 0~9에 숫자가 있으면 빼주기
            answer -= int(i) # 다빼고나면 없는 숫자만 더해진거로 출력
    
    return answer
