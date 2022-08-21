def solution(s):
    def split_(s):
        return list(s.split(','))

    s = s[2:-2]
    s = list(s.split('},{'))
    s = list(map(split_, s))
    for i, a in enumerate(s):
        s[i] = list(map(int, a))

    s.sort(key=lambda x: len(x))

    answer = []
    for a in s:
        for i in a:
            if i not in answer:
                answer.append(i)

    return answer
