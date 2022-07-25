from collections import deque


def solution(tickets):
    ticket = {}

    for (start, end) in tickets:
        ticket[start] = ticket.get(start, []) + [end]

    # µµÂøÁö ¾ËÆÄºª¼ø Á¤·Ä
    for i in ticket.keys():
        ticket[i].sort()

    deq = deque(["ICN"])
    answer = []

    while deq:
        top = deq[-1]

        if top not in ticket or len(ticket[top]) == 0:
            answer.append(deq.pop())
        else:
            deq.append(ticket[top][0])
            del ticket[top][0]

    return answer[::-1]
