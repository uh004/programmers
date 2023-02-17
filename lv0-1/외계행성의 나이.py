# 딕셔너리로 key,value로 만들고 num 리스트에 저장

def solution(age):
    a = {'0':'a','1':'b','2':'c','3':'d','4':'e','5':'f','6':'g','7':'h','8':'i','9':'j'}
    num = []
    for i in str(age):
        num.append(a[i])
    return ''.join(num)

# 인덱스를 활용해서 a = 0번째 b - 1번째여서 a 리스트에 숫자 넣기
def solution(age):
    answer = ['a','b','c','d','e','f','g','h','i','j']
    a = []
    age = str(age) # '23'
    for i in age:
        i = int(i)
        a.append(answer[i])
        
    return ''.join(a)
