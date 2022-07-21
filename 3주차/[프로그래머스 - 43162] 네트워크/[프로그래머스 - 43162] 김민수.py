checked = []
my_computers = []

def solution(n, computers):
    answer = 0
    global checked, my_computers
    my_computers = computers
    checked = [False for i in range(0, n)] 
    for j in range(0, n):
        if checked[j] == False:
            dfs(j) 
            answer += 1 
    return answer

def dfs(j):
    global checked
    if checked[j] == True: 
        return
    checked[j] = True
    for (idx, v) in enumerate(my_computers[j]):
        if v == 1:
            if checked[idx] == False: 
                dfs(idx)