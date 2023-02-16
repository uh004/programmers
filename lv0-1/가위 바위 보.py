# 가위 바위 보에서 이기는경우를  반환하는거
# 가위 -> 바위 바위 -> 보 보 -> 가위

def solution(rsp):
    answer = ''
    for i in rsp:
        if i == '2':
            answer += '0'
        elif i == '0':
            answer += '5'
        elif i == '5':
            answer += '2'
    return answer
# 리스트에 담아서 join으로 묶기 위에랑 비슷
def solution(rsp):
    answer = []
    for i in rsp:
        if i == '2':
            answer.append('0')
        elif i == '0':
            answer.append('5')
        elif i == '5':
            answer.append('2')
    return ''.join(answer)
# 딕셔너리를 활용해서 0 2 5를 출력하면 이기는 숫자 출
def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)
