from collections import deque


def solution(expression):
    expression = deque(expression)
    num = ""
    ex = []

    while expression:
        a = expression.popleft()
        if a in ["-", "*", "+"]:
            ex.append(int(num))
            ex.append(a)
            num = ""
        else:
            num += a

    ex.append(int(num))

    priority = [['+', '-', '*'], ['+', '*', '-'], ['-', '+', '*'],
                ['-', '*', '+'], ['*', '-', '+'], ['*', '+', '-']]

    def cal(oper, x, y):
        if oper == '+':
            return x+y
        elif oper == '-':
            return x-y
        else:
            return x*y

    answer = []

    for prior in priority:
        prior = deque(prior)
        exp = ex[:]
        for _ in range(3):
            op = prior.popleft()
            while op in exp:
                i = exp.index(op)
                an = cal(op, exp[i-1], exp[i+1])
                exp[i-1:i+2] = []
                exp.insert(i-1, an)

        answer.append(abs(int(exp[0])))

    return max(answer)
