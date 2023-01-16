# 가위 바위 보

def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)

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
