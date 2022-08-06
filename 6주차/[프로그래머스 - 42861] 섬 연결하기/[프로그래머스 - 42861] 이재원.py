from collections import deque


def solution(n, costs):
    # sort by cost
    costs = sorted(costs, key=lambda x: x[2])
    costs = deque(costs)

    # vertex
    v = set([i[0] for i in costs])
    v2 = set([i[1] for i in costs])
    v.update(v2)

    # make union-find dictionary
    connect = {i: i for i in v}

    # feat union-find

    def find(x):
        if connect[x] == x:
            return x
        connect[x] = find(connect[x])
        return connect[x]

    def union(x, y):
        rx = find(x)
        ry = find(y)
        if rx < ry:
            connect[ry] = rx
        else:
            connect[rx] = ry

    answer = 0
    for v1, v2, cost in costs:
        # same root vertex = in same set.
        # so, find(v1) == find(v2) : cycle occur.
        if find(v1) != find(v2):
            union(v1, v2)
            answer += cost

    return answer
