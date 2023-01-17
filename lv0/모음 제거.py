# 모음 제거

def solution(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])

def solution(my_string):
    answer = ''

    for c in my_string:
        if c in ['a', 'e', 'i', 'o', 'u']:
            continue
        answer += c

    return answer

def solution(my_string):
    answer = ''
    for i in my_string:
        if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
            answer += i
    return answer

def solution(my_string):
    A = ['a','e','i','o','u']
    answer = ''
    for i in my_string:
        if i not in A:
            answer += i

    return answer

def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in ['a','e','i','o','u']:
            answer += i


    return answer
