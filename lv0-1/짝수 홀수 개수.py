# num1 변수에는 짝수로 떨어지면 num2 변수에는 홀수로 떨어지면 마지막 리스트로 묶어서 반

def solution(num_list):
    num1 = 0
    num2 = 0
    
    for i in num_list:
        if i % 2 == 0:
            num1 += 1
        else:
            num2 += 1
    
    return [num1,num2]

# 리스트 인덱스를 활용해서 [0] 짝수 [1] 홀수를 더하게 
def solution(num_list):
    answer = [0,0]

    for num in num_list:
        if num % 2 == 0:
            answer[0] += 1
        else:
            answer[1] += 1

    return answer
