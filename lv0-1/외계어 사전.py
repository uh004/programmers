# spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가 dic에 존재한다면 1, 존재하지 않는다면 2

def solution(spell, dic):
    for i in dic: # dic에있는 문자열 하나씩 불러오기
        if sorted(i) == sorted(spell): # 문자열 정렬해서 하나씩 불러온 문자열과 spell 문자열이 같으면
            return 1 # 1로 반환
        
    return 2 # 없으면 2로 반환 여기서 if 밑에 else조건을 써버리면 오류
        
