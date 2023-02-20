def solution(array,n):
    answer = 0 # 제일 가까운 array값 
    number = 9999 # 비교 숫자
    array.sort() # 작은수부터 큰수까지 정렬
    for i in array: # 3 10 28
        if abs(i-n) < number: # 17 10 8 절대값으로 작으면 n과 가까움
            number = abs(n - i)
            answer = i
    return answer
