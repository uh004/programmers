# 짝수 홀수 개수

def solution(num_list):
    answer = [0,0]
    for i in num_list:
        if i % 2 == 0:
            answer[0] += 1
        else:
            answer[1] += 1
    return answer

def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer
