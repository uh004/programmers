def solution(num):
    cnt = 0
    
    while True:
        if num == 1: # 조건 나머지가 1이되면 멈춤
            break
        if cnt == 500: # 반복회수가 500이 되면 멈춤
            break
        if num %2 == 0: 
            num //= 2 # 짝수가 되면 몫을 나누고 다시 저장
            cnt += 1 # 카운트 1추가
        else:
            num = num * 3 + 1 # 홀수가 되면 3을 곱하고 1을 더한다.
            cnt += 1 # 카운트 1추가
            
    return cnt if cnt != 500 else -1 # 조건 cnt 카운트가 500이 되면 브레이크가 되니까 그전까지 그 값 출력 500이되면 -1 되는 식으로
