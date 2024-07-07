class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for i in range(m)]
        for row in range(m):
            for column in range(n):
                if row == 0 or column == 0:
                    dp[row][column] = 1
                else:
                    dp[row][column] = dp[row-1][column] + dp[row][column-1]
        return dp[m-1][n-1]

        