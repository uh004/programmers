def solution(t, p):
    answer = 0
    p_len = len(p) # 3
    for i in range(len(t)-p_len+1): # 7-3+1 5 0 1 2 3 4
        if int(t[i:i+p_len]) <= int(p): # 0 : 3 314 <= 271 1 : 4 141 2 : 5 415 3 : 6 159 4 : 7 592
            answer += 1 # 0 1 0 1 0 = 2
    return answer
