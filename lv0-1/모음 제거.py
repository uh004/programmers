# my_string 문자열을 하나씩 불러와서 모음 aeiou
# 안들어있으면 자음만 더하기

def solution(my_string):
    answer = ''
    
    for i in my_string:
        if i not in 'aeiou':
            answer += i
    return answer

# 여기는 모음을 만나면 continue로 건너띄기
def solution(my_string):
    answer = ''

    for c in my_string:
        if c in ['a', 'e', 'i', 'o', 'u']:
            continue
        answer += c

    return answer

# 한줄로 만들면 컴플레헨션을 통해서 ''.join으로 
def solution(my_string):
    return "".join([i for i in my_string if not i in "aeiou"])
