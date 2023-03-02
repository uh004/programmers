# a,b 사이 속한 정수 합 리턴

def solution(a, b):
    answer = 0
    
    if a > b: # 조건중에 a가 더 큰경우 비교해서 a가 더크면 b랑 교체해서
        tmp = a # tmp라는 빈 변수 만들고 a값 넣고
        a = b # a값을 b로 덮고
        b = tmp # tmp에 저장된 a값을 b로 저장
    
    for i in range(a,b+1): # a부터 b까지 속한 수 불러오기
        answer += i # 하나씩 다 더하기
    
    return answer
