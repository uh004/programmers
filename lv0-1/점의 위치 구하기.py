# x가 양수 y가 양수 1사분면
# x가 음수 y가 양수 2사분면
# x가 음수 y가 음수 3사분면
# x가 양수 y가 음수 4사분면

def solution(dot):
    if dot[0] > 0 and dot[1] > 0:
        return 1
    elif dot[0] < 0 and dot[1] > 0:
        return 2
    elif dot[0] < 0 and dot[1] < 0:
        return 3
    elif dot[0] > 0 and dot[1] < 0:
        return 4
