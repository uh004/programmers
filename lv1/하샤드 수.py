def solution(x):
    answer = 0 # 각 자리수 합 더하기
    for i in str(x): # 문자열로 바꿔서 하나씩 불러오기
        answer += int(i) # 불러온 숫자를 정수로 다 더해주기
    if x % answer == 0: # 다 더한 수에서 x를 나눠서 0으로 나눠 떨어지면 조건 실행
        return True
    else:
        return False
