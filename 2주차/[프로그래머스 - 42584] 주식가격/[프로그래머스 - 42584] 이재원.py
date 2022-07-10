def solution(prices):
    answer = [0]*len(prices)
    leng = len(prices)

    for i in range(leng):
        for j in range(i+1, leng):
            if prices[i] > prices[j]:
                answer[i] = j - i
                break
        if answer[i] == 0:
            answer[i] = leng-1 - i

    return answer
