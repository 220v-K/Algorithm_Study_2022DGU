from collections import defaultdict

def solution(tickets):
    answer = []
    routes = defaultdict(list)

    for [start, end] in tickets:
        routes[start].append(end)

    for k in routes.keys():
        routes[k].sort(reverse=True) #도착지 알파벳 역순으로 배열 
       
    stack = ["ICN"]
    while stack:
        start = stack[-1]

        if not routes[start]: #start에서 출발하는 티켓 없으면 
            answer.append(stack.pop())

        else:
            stack.append(routes[start].pop())

    return answer[::-1]
