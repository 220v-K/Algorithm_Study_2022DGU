from collections import deque


def solution(numbers, hand):
    isRight = True if (hand == "right") else False

    keyPad = {1: [1, 1], 2: [1, 2], 3: [1, 3],
              4: [2, 1], 5: [2, 2], 6: [2, 3],
              7: [3, 1], 8: [3, 2], 9: [3, 3],
              '*': [4, 1], 0: [4, 2], '#': [4, 3]}

    def distance(x, y):
        xDis = abs(keyPad[x][0] - keyPad[y][0])
        yDis = abs(keyPad[x][1] - keyPad[y][1])
        return xDis+yDis

    numbers = deque(numbers)
    answer = ""
    left = '*'
    right = '#'

    while numbers:
        num = numbers.popleft()

        if num in [1, 4, 7]:
            answer += "L"
            left = num
        elif num in [3, 6, 9]:
            answer += "R"
            right = num
        else:
            leftDis = distance(left, num)
            rightDis = distance(right, num)
            if leftDis < rightDis:
                answer += "L"
                left = num
            elif leftDis > rightDis:
                answer += "R"
                right = num
            else:   # leftDis == rightDis
                if isRight:
                    answer += "R"
                    right = num
                else:
                    answer += "L"
                    left = num

    return answer
