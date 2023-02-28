# 약수 구하는 식 ex 6 -> 1 2 3 6 
# 약수의 공통점은 6을 약수로 나누면 나눠 떨어진다.
# 1,n까지 숫자를 불러오고 나눠 떨어진거를 더해준다.

def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n % i == 0:
            answer += i
            
    return answer
