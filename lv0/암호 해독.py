# 암호 해독

def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer

def solution(cipher, code):
    answer = ''
    for i in cipher[code-1::code]:
        answer += i
    return answer
