# code번째 부터 암호로 인식
# 인덱스는 -1부터 해야 4번째니까 첫번째에 -1 하고 더해주기

def solution(cipher, code):
    answer = ''
    
    for i in cipher[code-1::code]:
        answer += i
        
    return answer
