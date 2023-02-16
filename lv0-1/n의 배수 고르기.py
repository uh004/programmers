# numlist 리스트를 하나씩 불러와서 n의 배수가 아닌것을
# if문으로 나눠서 떨어지면 answer리스트에 추가

def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0:
            answer.append(i)
            
    return answer
# 위에 코드를 컴플레헨션으로 한줄로 변경
def solution(n, numlist):
    answer = [i for i in numlist if i%n==0]
    return answer
