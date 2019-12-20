"""
198、打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，
计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
动态规划:
    dp = [0]+ [0] + [0]*n  表示数组长度为n时的最大收益
    dp[i] = max(dp[i-2] + nums[i], dp[i-1])  # 拿了当前这一个，上一个就不能拿
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        premax, curmax = 0, 0
        for num in nums:
            premax, curmax = curmax, max(premax+num, curmax)
        return curmax
