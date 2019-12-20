"""
34、在排序数组中查找元素的第一个位置和之后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。
找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。
示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
题解：O(log n)  二分法，查找到target, 左右走(最坏线性)
    模仿查小于等于目标值的最大值的位置，大于等于目标值最小值的位置就可以了。。
"""

class Solution:
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1

        return lo


    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]

    def higher_bound(self,nums, target):
        n = len(nums)
        imin, imax = 0, n - 1
        res = -1
        while imin < imax:
            mid = imin + (imax - imin) // 2
            if nums[mid] < target:
                imin = mid + 1
            elif nums[mid] > target:
                imax = mid
            else:
                res = mid
                imax = mid
        return res


    def searchRange2(self, nums, target) :
        n = len(nums)
        imin, imax = 0, n - 1
        first, last = -1, -1
        if not n:
            return [first, last]
        while imin < imax:
            mid = imin + (imax - imin)//2
            if nums[mid] < target:
                imin = mid + 1
            elif nums[mid] > target:
                imin = mid
            else:
                first, last = mid, mid
                while nums[first-1] == nums[mid]:
                    first -= 1
                while nums[last+1] == nums[mid]:
                    last += 1
                break
        return [first, last]


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.searchRange([5,7,7,8,8,10], 8))