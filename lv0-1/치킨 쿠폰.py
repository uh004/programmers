def solution(chicken):
    answer = 0 # 치킨쿠폰으로 시킨 개수
    
    while chicken >= 10: # 조건이 치킨 쿠폰 10장에 -> 치킨 한마리
        answer += chicken // 10 # 치킨쿠폰 10장당 한마리 치킨 개수
        number = chicken % 10 # 쿠폰 남은 개수
        chicken = chicken // 10 + number # 다시 쿠폰10개 -> 치킨한마리 
        
    return answer
