# for문으로 불러와서 길이만큼 answer에 담기

def solution(strlist):
    answer = []
    
    for i in strlist:
        answer.append(len(i))
    return answer

# 리스트 컴프리헨션으로 위에코드를 한줄로
def solution(strlist):
    return [len(str) for str in strlist]
