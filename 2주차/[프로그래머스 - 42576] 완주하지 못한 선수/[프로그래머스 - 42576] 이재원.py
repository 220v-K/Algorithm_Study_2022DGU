def solution(participant, completion):
    dic = {}
    for part in participant:
        val = dic.get(part, 0)
        dic[part] = val + 1

    for name in completion:
        dic[name] -= 1

    for key in dic.keys():
        if dic[key] == 1:
            return key
