# 리스트컴플리헨션으로 str(i)에 count함수를 사용해서 str(k)가 몇개있는지
# 마지막에 sum으로 다 더하기

def solution(i, j, k):
    answer = sum([str(i).count(str(k)) for i in range(i,j+1)])      
    return answer

# 이게 두자리 숫자에서 만약에 k가 1이고 i 11 이면 두번 더해야하는데 1번더함 그래서 오류
def solution(i, j, k):
    answer = 0
    for num in range(i,j+1):
        if str(k) in str(num): # 1 10 11 12 13
            answer += 1
            
    return answer

# 
def solution(i, j, k):
    answer = 0
    for num in range(i, j + 1):
        if str(k) in str(num):
            answer += str(num).count(str(k))
    return answer
# num에 str이 몇개 있는지 개수 세기 위에 거랑 동일 위에거는 if 조건이 있는데 없어도 가능 한거 같다.
def solution(i, j, k):
    answer = 0
    for num in range(i, j + 1):
        answer += str(num).count(str(k))
    return answer
