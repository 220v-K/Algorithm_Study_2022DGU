def solution(N, number):
    set_num = [set()]
    # i = 1 ~ 8
    for i in range(1, 9):
        set_i = set()

        if i == 1:
            set_i.add(N)
        elif i == 2:
            new = [N*11, N-N, N*N, N+N, int(N/N)]
            set_i.update(new)
        else:   # i = 3 ~ 8
            for j in range(1, i):
                for num1 in set_num[i-j]:
                    for num2 in set_num[i-(i-j)]:
                        new = [num1+num2, num1-num2, num1*num2]
                        if num2 != 0:
                            new.append(int(num1/num2))
                        set_i.update(new)

            no_symbol_num = int(str(N)*i)
            set_i.add(no_symbol_num)

        if number in set_i:
            return i

        set_num.append(set_i)

    return -1
