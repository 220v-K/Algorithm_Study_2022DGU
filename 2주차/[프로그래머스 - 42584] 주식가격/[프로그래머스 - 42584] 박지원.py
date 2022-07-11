from collections import deque
def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        tmp = queue.popleft()   #해당 큐의 맨 첫값 pop
        time = 0
        for p in queue:
            time += 1 # 1초 지났으므로 +1
            if tmp > p: # 떨어진경우
                break
                
        answer.append(time)
    

    return answer