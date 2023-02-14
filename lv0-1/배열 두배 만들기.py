# 리스트 컴프리헨션을 이용해서 하나씩 불러온 수를 곱하기 2를 해서 다시 반환

def solution(numbers):
    answer = [i * 2 for i in numbers]
    return answer

# append를 활용해서 answer에 곱하기 2에서 담기
def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(i*2)
    return answer
