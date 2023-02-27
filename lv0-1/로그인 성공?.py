# for문을 통한 비교
def solution(id_pw, db):
    for i in db: # i = ['아이디','비밀번호']
        if id_pw[0] in i: # id 여부 확인
            if id_pw[1] == i[1]: # 비밀번호가 같은지
                return "login" # 위조건에 아이디있고 비번도 있으면 login
            else:
                return "wrong pw" # 아이디는 있지만 비밀번호가 없으면 wrong pw
    return "fail" # 아무것도 없으면 fail
