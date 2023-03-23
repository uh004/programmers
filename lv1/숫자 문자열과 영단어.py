def solution(s):
    num = ['zero','one','two','three','four','five','six','seven','eight','nine']
    answer = ''
    for idx, i in enumerate(num): # 0 zero, 1 one
        if i in s: # zero 가 s 에 있으면
            s = s.replace(i,str(idx)) # zero를 0으로 교체
        answer = s # 교체된거 answr에다시 넣기 
    return int(answer) # 마지막 출력할때 int로 바꿔서 출력

def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)



def solution(s):
    num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
               
               
