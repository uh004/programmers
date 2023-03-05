# 가운데 글자 반환 길이가 짝수면 2개 홀수면 1개

def solution(s):
    answer = ''
    
    if len(s) % 2 == 1: # 홀수라면
        answer += s[len(s) // 2] # // 작대기 2개를 해야함 인덱스가 0부터사작해서
    elif len(s) % 2 == 0: # 짝수라면
        answer += s[len(s)//2 -1:len(s)//2+1] # 인덱스때면 -1 뺀 인덱스부터 +1 더한 인덱스까지 
        
    
    return answer
