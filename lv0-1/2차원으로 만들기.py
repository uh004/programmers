# answer에 넣고 cnt변수에 하나 넣을때 마다 하나씩 더하고
# 그 개수만큼 temp리스트에 넣고 다시 temp cnt 리셋시켜서
# 반복시키기

def solution(num_list, n):
    answer = []
    cnt = 0
    temp = []
    for num in num_list:
        temp.append(num)
        cnt += 1
        if cnt == n:
            answer.append(temp)
            temp = []
            cnt = 0

    return answer

# 0~n까지 answer에 넣기 그간격만큼 
def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer
