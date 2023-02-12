# for문을 이용해 안에 있는 리스트 하나씩 불러오고 머쓱이 키 if문을 이용해서 height < 변수 크면 카운트 세기

def solution(array, height):
    answer = 0
    for i in array:
        if height < i:
            answer += 1
    return answer

# 위에 코드를 컴프리헨션으로 1,1,1,1 키큰사람들 게속 누적 이걸 sum함수 사용해서 더하면 완료  
  
def solution(array, height):
    return sum(1 for a in array if a > height)
