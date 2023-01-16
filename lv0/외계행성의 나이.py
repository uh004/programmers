# 외계행성의 나이

def solution(age):
    answer = ['a','b','c','d','e','f','g','h','i','j']
    a = []
    age = str(age) # '23'
    for i in age:
        i = int(i)
        a.append(answer[i])
        
    return ''.join(a)

def solution(age):
    conv = {'0':'a','1':'b','2':'c','3':'d','4':'e'
            ,'5':'f','6':'g','7':'h','8':'i','9':'j'}
    return ''.join(conv[i] for i in str(age))
