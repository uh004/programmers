def solution(arr1, arr2):
    answer = [] # tmp [?,?], [?,?] 식으로 게속 저장
    for i in range(len(arr1)): # 전체 배열길이
        tmp = [] # 이중 for문 밑에 문장이 끝나고 다시 실행되면 빈 리스트로
        for j in range(len(arr1[0])): # 배열 안에 숫자 개수 0 1은 같으니 아무거나 해도 노상관
            tmp.append(arr1[i][j] + arr2[i][j]) # 0 0 0 0 [1+3] [2+4] / [2+5] [3+6]
        answer.append(tmp) # [4,6] answer에 저장  [7,9] answer에 저장
        
    return answer
