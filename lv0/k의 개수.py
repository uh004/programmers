# k의 개수

def solution(i, j, k):
    answer = 0
    for n in range(i, j + 1):
        answer += str(n).count(str(k))
    return answer


def solution(i, j, k):
    answer = sum([str(i).count(str(k)) for i in range(i,j+1)])      
    return answer
