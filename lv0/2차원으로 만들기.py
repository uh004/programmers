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
