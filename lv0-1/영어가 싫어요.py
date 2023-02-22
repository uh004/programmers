def solution(numbers):
    nums = ['zero','one','two','three','four','five','six','seven','eight','nine']
    
    for index, num in enumerate(nums): # index 0 num = zero 부터 하나씩 변수 담기 근데 start=100하면 시작값을 변경 가능
        numbers = numbers.replace(num, str(index)) # zero 몇에 인덱스를 교체해주기
    return int(numbers)

def solution(numbers):
    num = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',\
         'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for k in num.keys(): # 딕셔너리를 활용해서 key value 활용해서 키값만 불러오기
        numbers = numbers.replace(k, num[k]) # key를 key를 value로 교체

    return int(numbers)
