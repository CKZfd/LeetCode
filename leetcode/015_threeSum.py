"""
15、三数之和
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。
例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
题解：三数之和为0
    排序+双指针
    先对列表进行排序，升序 nums.sort()
    用i指向最小的数，则该数必须不大于0
    为了避免重复解，下一位相同时跳过
    令左指针 L=i+1，右指针 R=n−1，当 L<R 时，执行循环：
        当 nums[i]+nums[L]+nums[R]==0，执行循环，判断左界和右界是否和下一位置重复，
        去除重复解。并同时将 L,RL,RL,R 移到下一位置，寻找新的解
        若和大于 0，说明 nums[R]太大，R左移
        若和小于 0，说明 nums[L]太小，L右移

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        if (not nums or n<3):
            return []
        nums.sort()
        for i in range(n):
            if nums[i] > 0:
                return res
            # 避免重复解
            if i>0 and nums[i] == nums[i-1]:
                continue
            L = i + 1
            R = n - 1
            while L < R:
                sum = nums[i] + nums[L] + nums[R]
                if sum == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    # 避免重复解
                    while L<R and nums[L] == nums[L+1]:
                        L += 1
                    while L<R and nums[R] == nums[R-1]:
                        R -= 1
                elif sum > 0:
                    R -= 1
                else:
                    L += 1
        return res

