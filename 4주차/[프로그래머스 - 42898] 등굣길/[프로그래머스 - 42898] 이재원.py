def solution(m, n, puddles):
    puddles = list(map(lambda x: [x[1], x[0]], puddles))
    dp = [[0]*(m+1)]*(n+1)
    dp[1][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            elif [i, j] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[n][m] % 1000000007
