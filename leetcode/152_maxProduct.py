"""
152、乘积最大子序列
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列
（该序列至少包含一个数）。
示例 1:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:
输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
动态规划：
因为有负数的存在，我们保存当前位置的最大乘积，和最小乘积，
因为负数可以将最大乘积变最小，将最小变最大。
    1、dp[i],以当前i为结尾，的最大最小
    2、关系：
    3、初始条件：最大最小为1
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_res = float("-inf")
        max_num = 1
        min_num = 1
        for i in range(n):
            if nums[i] < 0:
                max_num, min_num = min_num, max_num
            max_num = max(max_num*nums[i], nums[i])
            min_num = min(min_num*nums[i], nums[i])
            max_res = max(max_res, max_num)
        return max_res


