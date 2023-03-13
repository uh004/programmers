from collections import deque

def solution(cacheSize, cities):
    l = [''] * cacheSize
    cache = deque(l, maxlen=cacheSize)
    answer = 0 # 시간
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            cache.append(city)
            answer += 5
    return answer

testcase = [
    [3, ['Jeju','Pangyo','Seoul','NewYork','LA','Jeju','Pangyo','Seoul','NewYork','LA']],
    [3, ['Jeju','Pangyo','Seoul','Jeju','Pangyo','Seoul','Jeju','Pangyo','Seoul']]
]

for case in testcase:
    print(solution(case[0], case[1]))
