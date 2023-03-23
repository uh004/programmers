def solution(strings, n):
    answer = []
                              
    strings = sorted(strings) # strings 배열 정렬
                              # 인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.
    arr = []                  # n번째 글자를 담을 배열
    
    for i in strings:
        arr.append(i[n])
    arr = sorted(arr)         # n번째 글자를 담은 배열을 정렬
    
    for i in arr:
        for j in strings:
            if i == j[n]:     # n번째 글자와 strings의 n번째 글자를 비교
                answer.append(j)
                strings.remove(j)
                break               # 반례 : ["aea", "ba", "ce", "aee"], 1
            
    
    return answer
