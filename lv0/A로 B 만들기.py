# A로 B 만들기

def solution(before, after):
    before = sorted(before)
    after = sorted(after)
    if before == after:
        return 1
    else:
        return 0

def solution(before, after):
    return 1 if sorted(before)==sorted(after) else 0

def solution(before, after):
    list_be = list(before)
    list_af = list(after)

    list_be.sort()
    list_af.sort()

    if list_be == list_af:
        answer = 1
    else:
        answer = 0

    return answer
