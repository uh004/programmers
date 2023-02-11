# 양꼬치 1인분 12000 음료수 1개당 2000
# 양꼬치 10인분을 먹으면 음료가 꽁짜
# 가격에 양꼬치 값x 개수 + 음료수 값 x 개수 + (양꼬치 10인분 먹으면 음료수 값 빼기)
# 그래서 양꼬치 개수를 10으로 나누기 나눈 몫 값 을 2000원 곱하기
# 만약에 10인분이 안넘으면 0*2000 = 0 근데 64개도 6인분으로 간주해서 //로 표시

def solution(n, k):
    answer = 0
    a = n // 10
    answer = (n * 12000) + (k * 2000) - (a * 2000)
    return answer

# 위에 코드를 간결하게 한줄로 가능하다.
def solution(n, k):
    return 12000 * n + 2000 * (k - n // 10)
