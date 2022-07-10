def solution(genres, plays):
    numOfgenre = set(genres)
    playBygenre = {}
    indexOfgenre = {}
    for i in range(len(genres)):
        gen = genres[i]
        play = plays[i]
        if gen in playBygenre:
            playBygenre[gen] += play
            indexOfgenre[gen].append([i, play])
        else:
            playBygenre[gen] = play
            indexOfgenre[gen] = [[i, play]]

    answer = []

    for _ in range(len(numOfgenre)):
        target = max(playBygenre, key=playBygenre.get)
        subindex = indexOfgenre[target]

        if len(indexOfgenre[target]) == 1:
            answer.append(subindex[0][0])
        else:
            subindex.sort(key=lambda x: (-x[1], x[0]))
            answer.append(subindex[0][0])
            answer.append(subindex[1][0])

        del playBygenre[target]

    return answer
