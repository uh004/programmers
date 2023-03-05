# 수박수박 n의 개수에따라 출력

def solution(n):
    answer = '수박' * 10000 # 조건이 n의 길이는 10000이하라서 수박을 * 10000을 해둠 수박수박수박......
    number = ''
    for i in answer[:n]: # answer에 수박수박.... n인덱스만큼 불러오기
        number += i # number에 그 개수만큼 더해주기
    
    return number
