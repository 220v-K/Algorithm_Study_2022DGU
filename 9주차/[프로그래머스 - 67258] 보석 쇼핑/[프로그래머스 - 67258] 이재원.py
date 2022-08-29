def solution(gems):
    gemList = {gems[0]: 1}
    start = 0
    end = 0
    answer = [0, len(gems)]

    kindOfGem = len(set(gems))

    def add(gem):
        if gem in gemList:
            gemList[gem] += 1
        else:
            gemList[gem] = 1

    def remove(gem):
        if gemList[gem] == 1:
            del gemList[gem]
        else:
            gemList[gem] -= 1

    while start <= end and end < len(gems):
        if kindOfGem == len(gemList):
            if answer[1]-answer[0] > end-start:
                answer = [start, end]
            remove(gems[start])
            start += 1

        elif kindOfGem != len(gemList):
            end += 1
            if end == len(gems):
                break
            add(gems[end])

    return [answer[0]+1, answer[1]+1]
