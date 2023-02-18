# 약수 구하려면 1~n까지 숫자를 나눠서 나머지가 0이 되면 약수가 된다

def solution(n):
    answer = []
    
    for i in range(1,n+1):
        if n % i == 0:
            answer.append(i)
    return answer
# 위에 코드를 컴플리헨션을 통해 한줄로 만들기
def solution(n):
    answer = [i for i in range(1,n+1) if n%i == 0]
    return answer
