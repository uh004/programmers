# 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *

def solution(phone_number):
    answer = '' 
    for i in range(len(phone_number)-4): # phone_number 길이에서 뒷자리 4개 제외
        answer += '*' # 나머지는 *로 채우고
    
    answer += phone_number[-4:] 마지막에 인덱스에서 -4부터-1까지 숫자만 불러오기
    
    return answer # 반환
