def solution(numbers, target):
    leng = len(numbers)

    def dfs(numbers, total, depth):
        if depth == leng:
            if total == target:
                return 1
            else:
                return 0
        else:
            a = dfs(numbers, total+numbers[depth], depth+1)
            b = dfs(numbers, total-numbers[depth], depth+1)
            return a+b

    return dfs(numbers, 0, 0)
