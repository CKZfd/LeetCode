"""
44. 通配符匹配
问题描述：
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。
说明:
	s 可能为空，且只包含从 a-z 的小写字母。
	p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
链接：https://leetcode-cn.com/problems/wildcard-matching
"""
"""
动态规划：
    1、定义数组的含义  dp[i][j] 表示s的前i个字符和p 的前j个字符是否匹配？
    2、找出数组元素之间的关系式：dp[i][j]和 dp[i-1] [j]、dp[i] [j-1]、dp[i-1] [j-1]的关系
        如果s的第i个字符与p的第j个字符匹配 if p[j] in {s[i], "?"} : dp[i][j]=dp[i-1][j-1]
        如果 p[j] == "*" :
            如果“*”匹配空字符串： dp[i][j]=dp[i][j-1]    
            如果“*”匹配多位    dp[i][j]=dp[i-1][j]
    3、找出初始值 
        当两者皆为空串时 dp[0][0] = True
        当s为空串时：dp[0][j] =       p为“*”时匹配
        当p为空串时 dp[i][0] = False
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False]*(n+1) for i in range(m+1)]
        dp[0][0] = True
        for j in range(1, n+1):
            if p[j-1] != "*":
                break
            else:
                dp[0][j] = True
        for i in range(1,m+1):
            for j in range(1, n+1):
                if p[j-1] in {s[i-1], "?"}:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
        return dp[-1][-1]


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.isMatch("aa", "*"))
