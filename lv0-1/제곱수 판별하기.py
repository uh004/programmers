# 제곱수를 확인하기 위해서 1부터 n번까지 수를 곱해서 그 곱한값이 n이랑 같은지 비교
# 맞으면 1 반환 아니면 2 반환

def solution(n):
    answer = 0
    for i in range(1,n):
        if i * i == n:
            return 1
    else:
        return 2
