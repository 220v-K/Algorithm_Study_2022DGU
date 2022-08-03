import heapq
import sys

read = sys.stdin.readline

N = int(read().strip("\n"))
lec = [list(map(int, read().strip("\n").split())) for _ in range(N)]

lec.sort()

# priorityQueue에는 종료시간을
q = []
heapq.heappush(q, lec[0][1])

for l in lec[1:]:
    if q[0] > l[0]:
        heapq.heappush(q, l[1])
    else:
        heapq.heappop(q)
        heapq.heappush(q, l[1])

print(len(q))
