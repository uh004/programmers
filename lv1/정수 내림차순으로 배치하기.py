# 정수 내림차순으로 배치하기 처음에 정수로 87616518 입력받움
# 문자열로 바꾸고 그러면 sorted 함수로 정렬하고 큰수부터 앞에오게 reverse
# 마지막 출력할때 리스트로 하나씩 되있는거 join으로 묶고 int로 바꿔서 출력

def solution(n):
    answer = 0
    
    n = sorted(str(n),reverse=True)
    
    
    return int(''.join(n))
