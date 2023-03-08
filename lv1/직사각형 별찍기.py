# 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

a, b = map(int, input().strip().split(' '))

for _ in range(b): # _ b 횟수
    print('*'*a) # a길이만큼 출력
