def solution(N, number):
    answer = -1 # 8보다 크면 -1을 return하기때문에
    num_list = [set() for x in range(8)] # 비어있는 집합 자료형 : set()
    
    for i,x in enumerate(num_list, start=1):
        x.add( int( str(N) * i ) ) # 5, 55, 555처럼 사칙연산없는 단순히 이어붙인 숫자 생성 
    
    if number in num_list[0]: # 바로 있는경우(즉, 답이 1인경우)
        return 1
    
    for i in range (1,8): # 2부터 8까지
        for j in range(i):
            for num1 in num_list[j]:
                for num2 in num_list[i-j-1]: # j가 0부터 시작해서 1을 더 빼줌 
                    num_list[i].add(num1+num2)
                    num_list[i].add(num1*num2)
                    num_list[i].add(num1-num2)
                    if num2 != 0:
                        num_list[i].add(num1/num2)
                        
        if number in num_list[i]:
            return i+1
                    
    return answer