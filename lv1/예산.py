def solution(d, budget):
    d.sort() # 1 2 3 4 5
    while budget < sum(d): # 9 < 15 -> [1 2 3 4] 5제외 다음 9 < 10 [1 2 3] 4 제외 9 < 6 
        d.pop()
        
    return len(d) # [1,2,3]길이
