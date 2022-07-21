def bfs(begin, target, words, visited):
    count = 0
    stack = [(begin, 0)]
    while stack:
        current, depth = stack.pop()
        if current == target:
            return depth
        
        for i in range(len(words)):
            if visited[i] == True:
                continue
            cnt = 0
            for a,b in zip(current, words[i]):
                if a!=b:
                    cnt += 1
            if cnt == 1:
                visited[i] = True
                stack.append((words[i], depth+1))
                
            

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0

    visited = [False]*(len(words))

    answer = bfs(begin, target, words, visited)

    return answer