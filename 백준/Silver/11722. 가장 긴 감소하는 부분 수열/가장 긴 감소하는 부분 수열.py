def longest_decreasing_subsequence(A):
    N = len(A)
    dp = [1] * N  # 모든 원소의 최소 길이는 1

    for i in range(N):
        for j in range(i):
            if A[j] > A[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    print(longest_decreasing_subsequence(A))
