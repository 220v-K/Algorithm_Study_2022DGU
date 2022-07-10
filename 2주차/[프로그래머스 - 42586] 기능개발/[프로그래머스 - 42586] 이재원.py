from collections import deque


def solution(progresses, speeds):
    deq = deque(progresses)
    deq_speed = deque(speeds)
    answer = []

    while len(deq) != 0:
        for i in range(len(deq)):
            deq[i] += deq_speed[i]

        cnt = 0
        while len(deq) > 0 and deq[0] >= 100:
            deq.popleft()
            deq_speed.popleft()
            cnt += 1

        if cnt > 0:
            answer.append(cnt)

    return answer
