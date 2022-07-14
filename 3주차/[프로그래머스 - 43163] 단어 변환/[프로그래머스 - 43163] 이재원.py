from collections import deque


def solution(begin, target, words):
    def canChange(fromWord, toWord):
        difChar = 0
        for i in range(len(fromWord)):
            if fromWord[i] == toWord[i]:
                continue
            else:
                difChar += 1

        if difChar == 1:
            return True
        else:
            return False

    if target not in words:
        return 0

    step = 0
    deq = deque([begin])
    stepDeq = deque([])

    while deq:
        step += 1

        while deq:
            start = deq.popleft()

            for word in words:
                if canChange(start, word):
                    stepDeq.append(word)

        deq.extend(stepDeq)
        stepDeq.clear()

        if target in deq:
            return step

    return 0
