answer = 0
def dfs(index, numbers, target, value):
    global answer
    n = len(numbers)
    if(index== n and target == value):
        answer += 1
        return
    if(index == n):
        return

    dfs(index+1,numbers,target,value+numbers[index])
    dfs(index+1,numbers,target,value-numbers[index])

def solution(numbers, target):
    global answer
    dfs(0,numbers,target,0)
    return answer
