#  seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다. 조건
# index로 Kim이 어딨는지 확인 그 인덱스 번호 number로 반환
# answer에 f스트링으로 출력

def solution(seoul):
    answer = ''
    
    number = seoul.index('Kim')
    
    answer = f"김서방은 {number}에 있다"

    
    return answer
