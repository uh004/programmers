def solution(s):
    answer = [] # 대문자 변경해서 저장 공간 
    s = s.split(' ') # 공백기준으로 나누기 ['try', 'hello', 'world]

    for i in range(len(s)): # 길이만큼 출력 3
        result = ''
        for j in range(len(s[i])): # try -> 길이 3
            if j % 2 == 0: # 0 2
                result += s[i][j].upper() # 0 0 / 0 2 짝수번째 대문자로
            else: # 1
                result += s[i][j].lower() # 0 1

        answer.append(result) # 'TrY'

    return ' '.join(answer)
