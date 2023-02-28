# 12345 -> [5,4,3,2,1] 변경
# 입력받은 n을 문자열로 바꾸고 리스트를 담아야 변경됨 그냥 리스트만 담으면 에러
# 리스트로 담은거를 인덱스를 활용햐서 -1로 하면 뒤에서부터 불러와서 answer에 담기

def solution(n):
    answer = []
    n = list(str(n))
    
    for i in n[::-1]:
        answer.append(int(i))
    
    
    return answer
