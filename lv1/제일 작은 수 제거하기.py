# 리스트 제일 작은 수 제거 만약에 리턴배열이 0이면 -1 출력

def solution(arr):
    if len(arr) > 1: # arr 배열 길이가 1보다 큰지 확인
        arr.remove(min(arr)) # 조건이 성립되면 min으로 제일 작은 값을 remover로 제거
        
        return arr
    else:
        return [-1] # 조건이 실행안되면 빈리스트라 추정 -1로 반환
