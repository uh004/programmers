def solution(arr):
    answer = []
    answer.append(arr[0]) # 첫번째 인덱스 값넣기
    
    for i in range(1, len(arr)): # 인덱스 1부터 arr 길이까지 출력
        if arr[i-1] != arr[i]: # i-1 과 i를 비교 전거와 지금거 이게 다르면 answer에 넣기
            answer.append(arr[i])

    return answer
