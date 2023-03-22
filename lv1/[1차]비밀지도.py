def solution(n, arr1, arr2):
    answer = []
    for i in range(n): # 5
        num = bin(arr1[i] | arr2[i]) # 9(01001),30(11110) or 이니까 0 1 중에 1이 있으면 1 11111
        num = num[2:].zfill(n) # 앞에 0b 인덱스 후부터 zfill(5) 5자리가 아니면 그자리 0으로 채우기 11111
        num = num.replace('1', '#').replace('0', ' ') # 11111 -> #####
        answer.append(num) # num 하나씩 저장
    return answer
