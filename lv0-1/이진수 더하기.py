def solution(bin1, bin2):
    num1 = int(bin1,2) # 문자열을 이진수로 바꾸기 그리고 정수형으로
    num2 = int(bin2,2) # 위와 같음
    
    answer = bin(num1 + num2) # num1과 num2의 값을 더하고 이진수로 변환
    
    return answer.replace('0b','') # 이진수로 변환하면 앞에 0b가 생기므로 replace로 '' 공백으로 변환하기
