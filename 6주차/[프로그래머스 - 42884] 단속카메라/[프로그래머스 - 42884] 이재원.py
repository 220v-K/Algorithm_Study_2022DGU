from collections import deque


def solution(routes):
    routes = deque(sorted(routes, key=lambda x: (x[1], x[0])))

    camera = -30001
    answer = 0
    while routes:
        car = routes.popleft()
        if camera >= car[0] and camera <= car[1]:
            continue
        else:
            camera = car[1]
            answer += 1

    return answer
