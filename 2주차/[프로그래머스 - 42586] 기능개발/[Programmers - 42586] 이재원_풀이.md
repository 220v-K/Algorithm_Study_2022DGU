# Programmers - 42586. 기능개발

## 접근

그냥.. 큐에 넣고

한 턴에 한번씩 모든 index의 값 speed만큼 증가시키면서

0번 index가 100 이상이 되었을 때 한번에 몇 개 빼는지 기록.

간단쓰

```python
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
```

