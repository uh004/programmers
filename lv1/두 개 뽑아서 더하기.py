def solution(numbers):
    answer = []
    
    for i in range(len(numbers)): # 2중 for 문으로 한번씩 다 더해주기
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j]) # 더한수 answer에 저장
    
    answer = list(set(answer)) # 중복된거 set으로 없애주고 다시 list로
    answer.sort() # 오름차순으로 정렬
    
    return answer
