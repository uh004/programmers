# 영어가 싫어요

def solution(numbers):
    nums = ['zero','one','two','three','four','five','six','seven','eight','nine']
    
    for index, num in enumerate(nums):
        numbers = numbers.replace(num, str(index))
    return int(numbers)

def solution(numbers):
    dic = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    i=0
    for word in dic:
        numbers = numbers.replace(word, str(i))
        i+=1
    return int(numbers)

def solution(numbers):
    r = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',\
         'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for k in r.keys():
        numbers = numbers.replace(k, r[k])

    return int(numbers)
