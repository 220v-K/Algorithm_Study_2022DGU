import sys
sys.setrecursionlimit(10000)


def solution(k, room_number):
    room = {}
    # Find 구현

    def find(x):
        if x not in room.keys():
            room[x] = x+1
            return x

        if room[x] == x:
            return x

        k = find(room[x])
        # Union-Find -> Root까지의 경로 압축 (line 13)
        room[x] = k
        return k

    # 시작
    answer = []
    for p in room_number:
        if p not in room.keys():
            room[p] = p+1
            answer.append(p)
        else:
            root = find(p)
            answer.append(root)

    return answer
