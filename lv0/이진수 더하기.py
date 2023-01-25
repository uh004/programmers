# 이진수 더하기

def solution(bin1, bin2):
    answer = bin(int(bin1,2) + int(bin2,2))[2:]
    return answer # 0b 시작해서 인덱스 2부터 시작

def solution(bin1, bin2):
    num1 = int(bin1,2)
    num2 = int(bin2,2)
    
    answer = bin(num1+num2)
    
    return answer.replace('0b','')
