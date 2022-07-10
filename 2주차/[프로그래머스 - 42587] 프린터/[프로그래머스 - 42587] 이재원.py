from collections import deque


def solution(priorities, location):
    # target location Ç¥½Ã
    prior = [[i, 0] for i in priorities]
    prior[location][1] = 1

    deq = deque(prior)
    answer = 0

    while True:
        if deq[0][0] == max(deq, key=lambda x: x[0])[0]:
            if deq[0][1] == 1:
                return answer + 1
            else:
                deq.popleft()
                answer += 1
        else:
            deq.rotate(-1)
