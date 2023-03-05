# a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다. (n은 a, b의 길이)

def solution(a, b):
    answer = 0
    
    for i in range(len(a)): # len(b)로 해두됨 둘이 길이는 같다
        answer += a[i] * b[i] # 인덱스 0부터 a길이까지 둘이 곱해서 answer에 더해주기
    
    return answer
