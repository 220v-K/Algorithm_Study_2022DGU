def solution(triangle):
    answer = 0
    
    for i in range(1,len(triangle)): # 층수
        for j in range(len(triangle[i])): # 해당 층수 배열
            if j == 0 : # 맨왼쪽
                triangle[i][j] = triangle[i-1][0] + triangle[i][j]
            elif j == i : # 맨 오른쪽 
                triangle[i][j] = triangle[i-1][-1] + triangle[i][j]
            else: # 나머지 
                triangle[i][j] = max(triangle[i-1][j-1],triangle[i-1][j]) + triangle[i][j]
    
    answer = max(triangle[-1]) # 마지막 인덱스에서 최대값 찾기 
    
    return answer