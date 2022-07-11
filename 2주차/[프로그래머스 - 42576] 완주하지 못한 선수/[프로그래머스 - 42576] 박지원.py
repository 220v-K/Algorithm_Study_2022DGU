
## 딕셔너리 미사용 
def solution(participant, completion):
    answer = ""
    participant.sort() #순서 정렬 
    completion.sort()
    
    for i in range(0,len(completion)):
        if(participant[i] != completion[i]): # 없는경우 발견 
            return participant[i]
    
    answer = participant[len(participant)-1]    # 발견하지 못한경우 마지막
    
    return answer
    
## 딕셔너리 사용
def solution(participant, completion):
    answer = ""
    
    dict = {}
    cnt = 0 #hash 값들의 합
    
    for i in range(0,len(participant)): # 각 hash값 구해서 더하기 
        dict[hash(participant[i])] = participant[i]
        cnt += hash(participant[i])
        
    for i in range(0,len(completion)): # 완주목록 hash값 구해서 빼기 
        cnt -= hash(completion[i])
    #완주하지 못한 사람의 hash값만 cnt변수에 남는다    
    return dict[cnt] 