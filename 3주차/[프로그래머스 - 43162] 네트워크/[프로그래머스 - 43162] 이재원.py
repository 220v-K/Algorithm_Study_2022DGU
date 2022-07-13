from collections import deque


def solution(n, computers):
    network = 0
    computer = set(range(n))
    visited = set()

    deq = deque([])

    for i in range(n):
        if i in visited:
            continue

        deq.append(i)
        network += 1
        while deq:
            target = deq.popleft()
            for i in computer - visited:
                if target != i and i not in visited and computers[target][i] == 1:
                    deq.append(i)
            visited.add(target)

    return network
