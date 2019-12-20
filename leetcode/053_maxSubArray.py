"""
53、最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和
示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
题解：动态规划：
    1、	1、定义数组的含义  dp[i] 表示以位置i为结尾时的最大和
    2、找出数组元素之间的关系式：
        dp[i] = max(dp[i-1]+nums[i], nums[i])
    3、找出初始值 
        dp[0] = nums[0] if nums[0]>0 else 0
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] = max(nums[i-1]+nums[i], nums[i])
        return max(nums)

