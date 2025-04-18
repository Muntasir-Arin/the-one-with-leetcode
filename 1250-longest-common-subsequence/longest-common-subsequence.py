class Solution:
  def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    m = len(text1)
    n = len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
      for j in range(n):
        dp[i + 1][j + 1] = (1 + dp[i][j] if text1[i] == text2[j]
                            else max(dp[i][j + 1], dp[i + 1][j]))

    return dp[m][n]