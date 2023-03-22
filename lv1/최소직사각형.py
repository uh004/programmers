def solution(sizes):
    w = [] # 가로 길이
    h = [] # 세로 길이
    
    for i in sizes: # [[?,?],[?,?]] 2차원 리스트인데 하나씩 불러오기
        if i[0] > i[1]: # i = [?,?] 식으로 불러와짐 인덱스 0,1 비교
            w.append(i[0]) # 0인덱스가 더크면 w 대입
            h.append(i[1]) # 작은 값을 h 대입
        else:
            w.append(i[1]) # 1인덱스가 더크면 w 대입
            h.append(i[0]) # 작은 값을 h 대입
    
    return max(w) * max(h) # max로 제일 큰값 2개 곱하기
