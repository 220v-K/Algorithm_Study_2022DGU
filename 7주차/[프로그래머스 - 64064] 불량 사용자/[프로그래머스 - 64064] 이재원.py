def solution(user_id, banned_id):
    def isSame(user, ban):
        if len(user) != len(ban):
            return False

        for i in range(len(ban)):
            if ban[i] == '*':
                continue
            else:
                if ban[i] != user[i]:
                    return False

        return True

    able = {i: [] for i in range(len(banned_id))}

    for i, ban in enumerate(banned_id):
        for user in user_id:
            if isSame(user, ban):
                able[i].append(user)

    AllList = []

    def dfs(a, i):
        if i == len(banned_id):
            temp = a[:]
            AllList.append(temp)
            return

        for user in able[i]:
            b = a[:]
            # 중복 피하기 (시간초과)
            if user in b:
                continue
            b.append(user)
            dfs(b, i+1)
            del b[0]

    dfs([], 0)

    return len(set(map(tuple, map(sorted, map(list, AllList)))))
