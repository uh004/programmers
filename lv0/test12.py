# 중앙값 구하기

def solution(array):
    array.sort()
    if int(len(array)) % 2 == 0:
        i = len(array) // 2
        j = i -1
        return (array[i] + array[j]) / 2
    else:
        i = int(len(array)) // 2
        return array[i]

  
# 파이썬으로 풀이했음
# 원소 개수가 홀수인 경우, 
# 원소 개수를 2로 나누었을때의 정수값이 중간값이 되고,
# (예: 원소갯수가 5라면, 5/2=2.5이고, 반올림한 정수는 3이됨. 즉, 리스트상 3번째 원소가 중간값임)  
# 원소 개수가 홀수인 경우, 
# 원소 개수를 2로 나누었을때의 정수값과 그 다음 정수의 평균값이 되는 것으로 계산함
# (얘: 원소갯수가 4라면, 4/2=2, 즉, 리스트상 2번째 원소와 3번째 원소의 평균값이 중간값임) 

# (예)list = [17, 37, 37, 47, 57]

list = [1,2,3,4,5,6]

if int(len(list)) % 2 == 0:
   i = int(len(list)/2)
   j = i + 1
   print(int((list[i] + list[j])/2))
else:
    i = int((len(list))/2)
    print(list[i])
