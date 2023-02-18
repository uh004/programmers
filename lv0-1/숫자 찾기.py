# num을 이루는 숫자 중에 k가 있으면 num의 그 숫자가 있는 자리 수
# for문으로 문자열로 바꿔서 하나씩 비교 조건에 같은 수가 되면 
# answer에 number 더한거 더하고 멈추기 같은수가없으면 -1

def solution(num, k):
    answer = -1
    number = 0
    
    for i in str(num):
        number += 1
        if int(i) == k:
            answer = number
            break
    return answer
# find함수를 활용해서 a 변수에 num에 k있는지 찾고 그 숫자 반환
def solution(num, k):
    answer = (str(num).find(str(k))+1)
    if answer == 0:
        answer = -1
    return answer
