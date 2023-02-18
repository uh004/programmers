# 약수의 개수가 세 개 이상인 수를 합성수 최소 4부터가 합성수 
# 주어진 n이하의 합성수 구하기
# 이중 for문을 이용해서 n까지 구하고 i % j로 나눠서 나눠떨어지면 +1해주고
# 더한값이 3과 같거나 크면 합성수로 포함 +1로 해서 num 반환

def solution(n):
    num = 0
    for i in range(2,n+1):
        answer = 0
        for j in range(1, i+1):
            if i % j == 0:
                answer += 1
                
        if answer >= 3:
            num += 1
    return num
    
