def max_stair_score(n, score):
    if n == 1:
        return score[0]
    if n == 2:
        return score[0] + score[1]

    dp = [0] * n
    dp[0] = score[0]
    dp[1] = score[0] + score[1]
    dp[2] = max(score[0] + score[2], score[1] + score[2])

    for i in range(3, n):
        dp[i] = max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i])

    return dp[n-1]

# 입력
n = int(input())
score = [int(input()) for _ in range(n)]

# 출력
print(max_stair_score(n, score))
