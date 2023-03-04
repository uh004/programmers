# sings에 true false가 있다 true가 실행되면 양수 false가 실행되면 음수

def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)): # 숫자 길이만큼 하나씩 인덱스로 불러오기
        if signs[i]: # true면 실행
            answer += absolutes[i] # answer에 양수 더해주기
        else:
            answer -= absolutes[i] # true가 아니라면 음수 더해주기
    
    return answer
