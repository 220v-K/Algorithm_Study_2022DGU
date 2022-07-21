def solution(N, number):
    answer = -1
    result_list = []

    for i in range(1, 9):
        numbers = set() #중복되지 않게
        numbers.add( int(str(N) * i) )
        
        for j in range(0, i-1):
            for x in result_list[j]:

                for y in result_list[-j-1]:
                    numbers.add(x + y)
                    numbers.add(x - y)
                    numbers.add(x * y)
                    
                    if y != 0:
                        numbers.add(x // y)

        if number in numbers:
            answer = i
            break
        
        result_list.append(numbers)

    return answer
