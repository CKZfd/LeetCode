"""
33、搜索螺旋排序数组
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O(log n) 级别。
示例 1:
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:
输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
"""
"""
题解：要求O(log n)  二分法
    升序列表发生旋转
    直接使用二分法，判断那个二分点,有几种可能性
        1、直接等于target
        2、在左半边的递增区域
            a. target 在 left 和 mid 之间
            b. 不在之间
        3、在右半边的递增区域
            a. target 在 mid 和 right 之间
            b. 不在之间
qita:
先用二分法找出最小值，也是那个分割点,例如 [4,5,6,7,0,1,2]，我们找出数字 0；
接下来判断 target 是在分割点的左边还是右边;
最后再使用一次二分法找出 target 的位置. 所以时间复杂度为：O(logn)


作者：powcai
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array/solution/sou-suo-xuan-zhuan-pai-xu-shu-zu-by-powcai/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    
"""
class Solution:
    def search(self, nums, target):
        imin, imax = 0, len(nums)-1
        if not nums:
            return -1
        while imin < imax:
            mid = imin + (imax - imin)//2
            if nums[mid] == target:
                return mid
            elif nums[imin]<nums[mid]:
                if nums[imin] <= target <nums[mid] or nums[imin]>=target>nums[mid]:
                    imax = mid
                else:
                    imin = mid + 1
            else:
                if nums[mid] < target <= nums[imax] or nums[mid]>target>=nums[imax]:
                    imin = mid + 1
                else:
                    imax = mid
        return imin if nums[imin] == target else -1

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.search([3,1], 1))