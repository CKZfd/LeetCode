"""
121、买卖股票的最佳时期
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），
设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。
示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
牛顿莱布尼兹公式：区间和跟求差可以相互转换。
    题目要求最大价格差，我们可以构造一个数组，
    prices[i]-prices[i-1],代表每日能获得的利润值，
    这个数组的最大连续子数组和就是最大利润，即最大价格差。
使用动态规划，
动态规划：
    1、dp[n] 以n元素为结尾的 子数组的最大和
    2、关系：dp[i] = max()
    3、初始条件
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        diff = [0] + [prices[i] - prices[i-1] for i in range(1,n)]
        for i in range(1,n):
            # 如果一段子数组的和<0，它必然不是最大子数组和的一部分
            diff[i] = max(diff[i-1]+diff[i], 0)
            max_profit = max(diff[i], max_profit)
        return max_profit