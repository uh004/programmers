# 조건이 가장 긴 변이 나머지 두변의 합보다 작아야하니까
# 큰 수 부터 정렬하고 [0] < [1] + [2] 조건이 맞으면 되니까 1 거짓이면 2로 반환  

def solution(sides):
    sides.sort(reverse=True)
    
    if sides[0] < sides[1] + sides[2]:
        return 1
    else:
        return 2
    
