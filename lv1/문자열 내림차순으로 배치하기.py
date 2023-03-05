def solution(s):
    answer = ''.join(sorted(s, reverse = True)) # 큰순으로 정렬하기 위해서 reverse로 
    return answer
