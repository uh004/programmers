def solution(n, t, m, timetable): # n 횟수 m 명수
    timetable = sorted([int(i[:2]) * 60 + int(i[3:]) for i in timetable])
    
    콘의출근시간 = 540
    셔틀버스시간 = 540
    
    for i in range(n):
        for j in range(m):
            if timetable and timetable[0] <= 셔틀버스시간:
                콘의출근시간 = timetable.pop(0) - 1
            else:
                콘의출근시간 = 셔틀버스시간
        셔틀버스시간 = 셔틀버스시간 + t
            
    return f'{str(콘의출근시간//60).zfill(2)}:{str(콘의출근시간%60).zfill(2)}'


testcase = [
        (1, 1, 5, ['08:00', '08:01', '08:02','08:03']),
        (2, 10, 2, ['09:10', '09:09', '08:00']),
        (1, 2, 1, ['09:00','09:00','09:00','09:00'])
]

for n, t, m, timetable in testcase:
    print(solution(n, t, m, timetable))
