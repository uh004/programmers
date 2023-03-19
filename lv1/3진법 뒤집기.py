def solution(n):
    answer = ''

    while n > 0:			
        n, re = divmod(n,3)	# n을 3으로 나눈 몫과 나머지
        answer += str(re)
    return int(answer, 3)

# divmod() : 몫과 나머지를 리턴합니다. 리턴 값이 2개이므로 튜플을 사용합니다.
# int(x, base) : base 진법으로 구성된 str 형식의 수를 10진법으로 변환해 줌

def solution(n):
    tmp = ''
    while n: # 45 15 5 1 0 0이되면 False로 되서 반복문 빠져나감
        tmp += str(n % 3) # '0' '00' '0021'
        n = n // 3 # 15 5 1 0

    answer = int(tmp, 3) # tmp = '0021', 3
    return answer
