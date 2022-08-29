from collections import deque


def solution(n, path, order):
    pre = {i[0]: i[1] for i in order}
    follow = {i[1]: i[0] for i in order}

    visit = set([0])
    rooms = deque([0])
    rooms_wait = set()  # 선행조건때문에 못 가는 방 넣어두기
    graph = {i: [] for i in range(n)}

    for p in path:
        graph[p[0]].append(p[1])
        graph[p[1]].append(p[0])

    while rooms:
        room = rooms.popleft()

        # 선행 이행 X
        if room in follow:
            rooms_wait.add(room)
        # 걸리는 조건이 없을 때
        else:
            visit.add(room)
            # 선행조건 해결
            if room in pre:
                i = pre[room]
                del pre[room]
                if i in rooms_wait:
                    rooms.append(i)
                    rooms_wait.remove(i)
                del follow[i]

            for n in graph[room]:
                if n not in visit and n not in rooms_wait and n != room:
                    rooms.append(n)

    if rooms_wait:
        return (False)
    else:
        return (True)
