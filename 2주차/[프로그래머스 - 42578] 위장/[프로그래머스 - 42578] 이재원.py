def solution(clothes):
    closet = {}

    for cloth in clothes:
        if closet.get(cloth[1], -1) == -1:
            closet[cloth[1]] = 1
        else:
            closet[cloth[1]] += 1

    answer = 1
    for i in closet:
        answer *= closet[i] + 1

    return answer - 1
