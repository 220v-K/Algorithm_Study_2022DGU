def solution(priorities, location):
    answer = 0
    queue = [(i,p) for i,p in enumerate(priorities)]
    
    while(len(queue) != 1):
        j = queue.pop(0)
        if j[1] >= max(t[1] for t in queue): # 대기목록의 최댓값보다 큰경우 출력
            answer += 1
            if j[0] == location:
                return answer
        else:
            queue.append(j)
    
    # 하나 남은 경우 
    answer += 1
    return answer