# 1번 워밍업 문제(google)
## 1부터 10,000까지 8이라는 숫자가 총 몇번 나오는가?
## 8이 포함되어 있는 숫자의 갯수를 카운팅 하는 것이 아니라 8이라는 숫자를 모두 카운팅 해야 한다. (예를들어 8808은 3, 8888은 4로 카운팅 해야함)

str(list(range(1,10001))).count('8')

count = 0
for i in range(10001):
    if '8' in str(i):
        count += str(i).count('8')
        
print(count)

str([i for i in range(10001)]).count('8')
