def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit(): # 조건이 s의 길이가 4 혹은 6이고 # 문자열에 숫자만 있으면 true 
      # 문자가있으면 false 반환 문자안에 숫자 판별함수는 변수.isdigit()
        return True
    else:
        return False
