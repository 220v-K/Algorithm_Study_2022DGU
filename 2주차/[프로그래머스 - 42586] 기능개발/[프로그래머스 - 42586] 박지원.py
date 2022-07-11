import math
def solution(progresses, speeds):
    answer = []
    queue = []
    for p, s in zip(progresses, speeds):
        queue.append(math.ceil((100-p)/s)) #남은일수 계산 , 반올림 사용
    
    cnt = 0
    while queue: #queue가 비어있지 않으면 계속 진행
        if cnt == 0: # 배포 다음날
            tmp = queue.pop(0)
            cnt += 1
            continue
        if tmp < queue[0]: # 다음 기능이 완료 안된 경우
            answer.append(cnt)
            cnt = 0
        else:   # 다음 기능이 완료된 경우 
            cnt += 1
            queue.pop(0)
    
    answer.append(cnt)

    
    return answer