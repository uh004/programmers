# 머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
# 10만원 이상이면 그 값에다 0.05퍼 할인 값을 빼고 30만원 이상이면 0.1 50만원 이상은 0.2를 빼준 값을 다시 반환

def solution(price):
    if price >= 100000 and price < 300000:
        price = int(price - (price * 0.05))
    elif price >= 300000 and price < 500000:
        price = int(price - (price * 0.1))
    elif price >= 500000:
        price = int(price - (price * 0.2))
    return price
