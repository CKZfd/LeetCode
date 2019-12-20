class Solution:
    def dynaticP(self, n):
        if n <= 2:
            return n
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        print(dp)
        return dp[n]

    def uniquePaths(self, m, n):
        dp = [[0] * (n + 1) for i in range(m + 1)]
        dp[:][0] = 1
        dp[0][:] = 1
        print(dp)

if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(8,8))