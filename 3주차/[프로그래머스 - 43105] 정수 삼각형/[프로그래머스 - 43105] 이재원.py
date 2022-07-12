def solution(triangle):
    dp = [[triangle[0][0]]]

    for F in range(1, len(triangle)):
        now = []

        # F층에서
        for i in range(len(triangle[F])):
            num = triangle[F][i]
            num1, num2 = 0, 0
            # F-1 층의 내려올 수 있는 원소 2개
            # i=0일 때와 i=F일 때 예외처리 필요
            if i == 0:
                num1 = dp[F-1][i]
            elif i == F:
                num1 = dp[F-1][i-1]
            else:
                num1, num2 = dp[F-1][i-1], dp[F-1][i]

            now.append(max([num1, num2])+num)
        dp.append(now)

    return max(map(max, dp))
